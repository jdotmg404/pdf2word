# PDF 转 Word 工具

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/downloads/)

![Language](https://img.shields.io/badge/language-English%20%7C%20%E4%B8%AD%E6%96%87-blue)

[English](./README_EN.md) · [简体中文](./README_CN.md)

一个简单易用的 PDF 转 Word 在线转换工具，支持实时进度显示和自定义保存位置。

## 功能特性

- 🚀 **快速转换**：基于 pdf2docx 库，高效转换 PDF 文件
- 📊 **实时进度**：显示转换进度（第 X/Y 页 + 百分比）
- 💾 **自定义保存**：转换完成后可选择本地磁盘的任意保存位置
- 🎨 **简洁界面**：简单直观的用户界面

## 安装

### 环境要求

- Python 3.10+
- conda（推荐）或 pip

### 安装依赖

```bash
# 使用 conda（推荐）
conda create -n pdf2word python=3.10
conda activate pdf2word
pip install -e .

# 或使用 uv
uv sync
```

## 使用方法

### 1. 启动后端服务

```bash
conda activate pdf2word
python backend/app.py
```

服务器将在 `http://127.0.0.1:5000` 启动。

### 2. 启动前端服务

```bash
conda activate pdf2word
python -m http.server 8080 --directory frontend
```

### 3. 访问应用

在浏览器中打开 `http://localhost:8080`

### 4. 转换文件

1. 点击"选择文件"按钮，选择要转换的 PDF 文件
2. 点击"开始转换"按钮
3. 观察实时转换进度（显示当前页数/总页数 + 百分比）
4. 转换完成后，文件会自动下载

## 项目结构

```
pdf2word/
├── backend/
│   └── app.py              # Flask 后端服务器
├── frontend/
│   └── index.html          # 前端页面
├── pyproject.toml          # Python 依赖配置
└── README.md              # 项目说明
```

## 技术栈

### 后端
- **Flask**: Web 框架
- **Flask-CORS**: 跨域支持
- **pdf2docx**: PDF 转 Word 核心库
- **SSE**: Server-Sent Events 实时进度推送

### 前端
- **HTML5**: 页面结构
- **CSS3**: 样式设计
- **JavaScript (ES6+)**: 交互逻辑，Fetch API + ReadableStream

## API 接口

### POST /convert-stream

SSE 流式转换端点，实时推送转换进度。

**请求:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (PDF file)

**响应:**
- Content-Type: text/event-stream
- 事件类型:
  - `progress`: 进度更新
  - `complete`: 转换完成，包含 download_id
  - `error`: 错误信息

**进度事件示例:**
```json
{
  "stage": "parsing",
  "message": "正在解析... 第 5/10 页",
  "current": 5,
  "total": 10,
  "percent": 50
}
```

### GET /download/<download_id>

下载转换完成的文件。

**响应:**
- Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
- Body: Word 文件内容

### POST /convert

同步转换端点（保留兼容）。

## 常见问题

### Q: 转换速度慢怎么办？
A: 转换速度取决于 PDF 文件的大小和复杂度。现在有实时进度显示，可以清楚看到转换进度。

### Q: 转换后的格式不正确？
A: pdf2docx 对某些复杂的 PDF 格式支持有限。建议使用标准格式的 PDF 文件。

### Q: 如何修改端口？
A: 修改 `backend/app.py` 中的 `app.run(port=5000)` 端口号。

### Q: 下载的文件保存在哪里？
A: 转换完成后，浏览器会弹出保存对话框，您可以选择保存到本地磁盘的任意位置。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 致谢

- [pdf2docx](https://github.com/dothinking/pdf2docx) - PDF 转 Word 核心库
- [Flask](https://flask.palletsprojects.com/) - Web 框架

## 联系方式

如有问题或建议，请提交 Issue。

---

**注意**: 本工具仅用于学习和个人使用，请勿用于商业用途。