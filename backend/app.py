import os
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

    # 2. 准备路径
    temp_pdf_path = os.path.join(os.getcwd(), f"temp_{file.filename}")
    file.save(temp_pdf_path)

    # 构造输出的 Word 文件名和全路径
    docx_filename = file.filename.rsplit('.', 1)[0] + ".docx"
    output_docx_path = os.path.join(os.getcwd(), f"temp_{docx_filename}")

    try:
        # 3. 调用核心转换引擎
        cv = Converter(temp_pdf_path)
        cv.convert(output_docx_path, start=0, end=None)
        cv.close()

        # 4. 返回文件供下载
        return send_file(
            output_docx_path,
            as_attachment=True,
            download_name=docx_filename,
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    except Exception as e:
        return jsonify({"error": f"转换失败: {str(e)}"}), 500
    
    finally:
        # 5. 清理临时文件
        # 只删除PDF临时文件，Word文件在发送完成后会自动释放
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
        # 注意：Word文件在send_file完成后会自动释放，无需立即删除
        # 如果需要，可以考虑使用后台任务定时清理临时文件

if __name__ == '__main__':
    # 本地启动：默认 5000 端口
    print("服务器已启动，转换后的文件将通过浏览器下载")
    app.run(port=5000, debug=True)