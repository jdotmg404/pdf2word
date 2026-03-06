import os
import tempfile
import shutil
from io import BytesIO
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pdf2docx import Converter

app = Flask(__name__)
CORS(app)  # 允许前端跨域访问

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
