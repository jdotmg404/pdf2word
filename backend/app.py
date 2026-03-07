import os
import tempfile
import shutil
import uuid
import json
from io import BytesIO
from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
from pdf2docx import Converter

app = Flask(__name__)
CORS(app)  # 允许前端跨域访问

# 存储转换完成的文件（生产环境应使用 Redis 等）
converted_files = {}


def send_event(event_type, data):
    """发送 SSE 事件"""
    return f"event: {event_type}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


@app.route('/convert-stream', methods=['POST'])
def convert_stream():
    """SSE 流式转换端点，实时推送进度"""

    # 在请求上下文中获取文件并保存
    if 'file' not in request.files:
        return Response(
            send_event('error', {'error': '未选择文件'}),
            mimetype='text/event-stream'
        )

    file = request.files['file']
    if file.filename == '':
        return Response(
            send_event('error', {'error': '文件名不能为空'}),
            mimetype='text/event-stream'
        )

    # 在请求上下文中保存文件
    temp_dir = tempfile.mkdtemp()
    temp_pdf_path = os.path.join(temp_dir, f"temp_{file.filename}")
    file.save(temp_pdf_path)
    original_filename = file.filename

    def generate():
        nonlocal temp_dir
        try:

            # 2. 加载 PDF 并获取页数
            yield send_event('progress', {
                'stage': 'loading',
                'message': '正在加载 PDF...',
                'percent': 5
            })

            cv = Converter(temp_pdf_path)
            total_pages = len(cv.fitz_doc)

            if total_pages == 0:
                cv.close()
                yield send_event('error', {'error': 'PDF 文件没有页面'})
                return

            yield send_event('progress', {
                'stage': 'loading',
                'message': f'PDF 加载完成，共 {total_pages} 页',
                'percent': 10,
                'total': total_pages
            })

            # 3. 分析文档
            yield send_event('progress', {
                'stage': 'analyzing',
                'message': '正在分析文档结构...',
                'percent': 15,
                'total': total_pages
            })

            # 获取默认设置
            settings = cv.default_settings
            settings['ignore_page_error'] = True  # 忽略单页错误

            cv.load_pages()

            yield send_event('progress', {
                'stage': 'analyzing',
                'message': '文档分析完成',
                'percent': 20,
                'total': total_pages
            })

            cv.parse_document(**settings)

            # 4. 解析页面（20% - 80%）
            pages_to_parse = [page for page in cv.pages if not page.skip_parsing]
            num_pages = len(pages_to_parse)

            for i, page in enumerate(pages_to_parse, start=1):
                pid = page.id + 1
                # 计算进度：20% + (页数进度 * 60%)
                percent = 20 + int((i / num_pages) * 60)

                yield send_event('progress', {
                    'stage': 'parsing',
                    'message': f'正在解析... 第 {i}/{num_pages} 页',
                    'current': i,
                    'total': num_pages,
                    'percent': percent
                })

                try:
                    page.parse(**settings)
                except Exception as e:
                    # 忽略单页错误继续处理
                    print(f"解析页面 {pid} 时出错: {e}")

            # 5. 生成 Word（80% - 100%）
            yield send_event('progress', {
                'stage': 'creating',
                'message': '正在生成 Word 文档...',
                'percent': 85,
                'total': total_pages
            })

            # 创建输出文件
            docx_filename = original_filename.rsplit('.', 1)[0] + ".docx"
            temp_docx_path = os.path.join(temp_dir, "output.docx")

            # 获取已解析的页面
            parsed_pages = [page for page in cv.pages if page.finalized]
            num_parsed = len(parsed_pages)

            for i, page in enumerate(parsed_pages, start=1):
                percent = 85 + int((i / num_parsed) * 10)
                yield send_event('progress', {
                    'stage': 'creating',
                    'message': f'正在生成... 第 {i}/{num_parsed} 页',
                    'current': i,
                    'total': num_parsed,
                    'percent': percent
                })

            cv.make_docx(temp_docx_path, **settings)
            cv.close()

            # 6. 读取文件并生成下载 ID
            yield send_event('progress', {
                'stage': 'finalizing',
                'message': '准备下载...',
                'percent': 98,
                'total': total_pages
            })

            download_id = str(uuid.uuid4())
            with open(temp_docx_path, 'rb') as f:
                converted_files[download_id] = {
                    'data': f.read(),
                    'filename': docx_filename
                }

            # 清理临时目录（保留转换结果在内存中）
            shutil.rmtree(temp_dir, ignore_errors=True)

            # 7. 完成
            yield send_event('complete', {
                'message': '转换完成！',
                'percent': 100,
                'download_id': download_id,
                'filename': docx_filename
            })

        except Exception as e:
            yield send_event('error', {'error': f'转换失败: {str(e)}'})
        finally:
            if temp_dir and os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)

    return Response(generate(), mimetype='text/event-stream')


@app.route('/download/<download_id>', methods=['GET'])
def download_file(download_id):
    """下载转换完成的文件"""
    if download_id not in converted_files:
        return jsonify({"error": "文件不存在或已过期"}), 404

    file_info = converted_files.pop(download_id)  # 下载后删除
    buffer = BytesIO(file_info['data'])
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=file_info['filename'],
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

@app.route('/convert', methods=['POST'])
def handle_conversion():
    # 1. 检查文件
    if 'file' not in request.files:
        return jsonify({"error": "未选择文件"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "文件名不能为空"}), 400

    # 2. 使用系统临时目录
    temp_dir = tempfile.mkdtemp()
    temp_pdf_path = os.path.join(temp_dir, f"temp_{file.filename}")
    file.save(temp_pdf_path)

    # 构造输出的 Word 文件名
    docx_filename = file.filename.rsplit('.', 1)[0] + ".docx"

    try:
        # 3. 调用核心转换引擎，输出到内存缓冲区
        cv = Converter(temp_pdf_path)
        
        # 创建内存缓冲区
        output_buffer = BytesIO()
        
        # 先转换到临时文件，然后读取到内存
        temp_docx_path = os.path.join(temp_dir, "temp_output.docx")
        cv.convert(temp_docx_path, start=0, end=None)
        cv.close()
        
        # 读取到内存缓冲区
        with open(temp_docx_path, 'rb') as f:
            output_buffer.write(f.read())
        output_buffer.seek(0)

        # 4. 从内存返回文件供下载
        return send_file(
            output_buffer,
            as_attachment=True,
            download_name=docx_filename,
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    except Exception as e:
        return jsonify({"error": f"转换失败: {str(e)}"}), 500
    
    finally:
        # 5. 清理整个临时目录（包括PDF和Word临时文件）
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == '__main__':
    # 本地启动：默认 5000 端口
    print("服务器已启动，转换后的文件将通过浏览器下载")
    app.run(port=5000, debug=True)
