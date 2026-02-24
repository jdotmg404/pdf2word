# PDF 转 Word 工具 / PDF to Word Converter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/downloads/)

一个简单易用的 PDF 转 Word 在线转换工具，支持实时显示转换进度。

A simple and easy-to-use online PDF to Word conversion tool with real-time progress display.

## 功能特性 / Features

- 🚀 **快速转换**：基于 pdf2docx 库，高效转换 PDF 文件
- 📊 **实时进度**：显示真实的转换进度（当前页/总页数）
- 💾 **自定义保存**：转换完成后可选择本地磁盘的任意保存位置
- 🌐 **跨平台**：支持 Windows、Linux、macOS
- 🎨 **简洁界面**：简单直观的用户界面

- 🚀 **Fast Conversion**: Based on pdf2docx library for efficient PDF conversion
- 📊 **Real-time Progress**: Display actual conversion progress (current page/total pages)
- 💾 **Custom Save Location**: Choose any local disk location to save converted files
- 🌐 **Cross-platform**: Supports Windows, Linux, macOS
- 🎨 **Clean Interface**: Simple and intuitive user interface

## 截图 / Screenshot

![转换界面](screenshot.png)

## 安装 / Installation

### 环境要求 / Requirements

- Python 3.7+
- pip 或 conda

### 安装依赖 / Install Dependencies

```bash
# 使用 pip / Using pip
pip install -r requirements.txt

# 使用 conda / Using conda
conda create -n pdf2word python=3.8
conda activate pdf2word
pip install -r requirements.txt
```

## 使用方法 / Usage

### 1. 启动后端服务 / Start Backend Server

```bash
python backend/app.py
```

服务器将在 `http://127.0.0.1:5000` 启动。

The server will start at `http://127.0.0.1:5000`.

### 2. 启动前端服务 / Start Frontend Server

```bash
# 方法 1: 使用 Python HTTP 服务器 / Method 1: Using Python HTTP Server
python -m http.server 8080 --directory frontend

# 方法 2: 直接打开 index.html / Method 2: Open index.html directly
# 在浏览器中打开 frontend/index.html
# Open frontend/index.html in your browser
```

### 3. 访问应用 / Access the Application

在浏览器中打开 `http://localhost:8080`

Open `http://localhost:8080` in your browser.

### 4. 转换文件 / Convert Files

1. 点击"选择文件"按钮，选择要转换的 PDF 文件
2. 点击"开始转换"按钮
3. 等待转换完成，查看实时进度
4. 转换完成后，点击"下载文件"按钮
5. 选择保存位置，文件将保存到指定位置

1. Click the "Choose File" button to select a PDF file
2. Click the "Start Conversion" button
3. Wait for conversion to complete and view real-time progress
4. After conversion, click the "Download File" button
5. Choose the save location, and the file will be saved to the specified location

## 项目结构 / Project Structure

```
pdf2word/
├── backend/
│   └── app.py              # Flask 后端服务器 / Flask backend server
├── frontend/
│   └── index.html          # 前端页面 / Frontend page
├── requirements.txt        # Python 依赖 / Python dependencies
└── README.md              # 项目说明 / Project documentation
```

## 技术栈 / Tech Stack

### 后端 / Backend
- **Flask**: Web 框架 / Web framework
- **Flask-CORS**: 跨域支持 / CORS support
- **pdf2docx**: PDF 转 Word 核心库 / PDF to Word conversion library

### 前端 / Frontend
- **HTML5**: 页面结构 / Page structure
- **CSS3**: 样式设计 / Styling
- **JavaScript (ES6+)**: 交互逻辑 / Interactive logic
- **Server-Sent Events (SSE)**: 实时进度推送 / Real-time progress streaming

## API 接口 / API Endpoints

### POST /convert
上传 PDF 文件并开始转换，返回实时进度流。

Upload PDF file and start conversion, returns real-time progress stream.

**请求 / Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (PDF file)

**响应 / Response:**
- Content-Type: text/event-stream
- Events:
  - `start`: 转换开始，包含总页数 / Conversion started, includes total pages
  - `progress`: 进度更新，包含当前页和总页数 / Progress update, includes current and total pages
  - `complete`: 转换完成，包含文件名 / Conversion completed, includes filename
  - `error`: 错误信息 / Error message

### GET /download/<filename>
下载转换后的 Word 文件。

Download the converted Word file.

**请求 / Request:**
- Method: GET
- Parameter: filename (文件名 / filename)

**响应 / Response:**
- Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
- Body: Word 文件内容 / Word file content

## 常见问题 / FAQ

### Q: 转换速度慢怎么办？/ A: What if conversion is slow?
A: 转换速度取决于 PDF 文件的大小和复杂度。建议使用较小的文件进行测试。

A: Conversion speed depends on the size and complexity of the PDF file. It's recommended to test with smaller files.

### Q: 转换后的格式不正确？/ A: What if the converted format is incorrect?
A: pdf2docx 对某些复杂的 PDF 格式支持有限。建议使用标准格式的 PDF 文件。

A: pdf2docx has limited support for some complex PDF formats. It's recommended to use PDF files with standard formatting.

### Q: 如何修改端口？/ A: How to change the port?
A: 修改 `backend/app.py` 中的 `app.run(port=5000)` 端口号。

A: Modify the port number in `app.run(port=5000)` in `backend/app.py`.

## 贡献 / Contributing

欢迎提交 Issue 和 Pull Request！

Issues and Pull Requests are welcome!

## 许可证 / License

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 致谢 / Acknowledgments

- [pdf2docx](https://github.com/dothinking/pdf2docx) - PDF 转 Word 核心库
- [Flask](https://flask.palletsprojects.com/) - Web 框架

## 联系方式 / Contact

如有问题或建议，请提交 Issue。

If you have any questions or suggestions, please submit an Issue.

---

**注意 / Note**: 本工具仅用于学习和个人使用，请勿用于商业用途。

**Note**: This tool is for learning and personal use only. Please do not use it for commercial purposes.
