# PDF to Word Converter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/downloads/)

A simple and easy-to-use online PDF to Word conversion tool with real-time progress display and custom save location support.

## Features

- 🚀 **Fast Conversion**: Based on pdf2docx library for efficient PDF conversion
- 📊 **Real-time Progress**: Display conversion progress (Page X/Y + percentage)
- 💾 **Custom Save Location**: Choose any local disk location to save converted files
- 🎨 **Clean Interface**: Simple and intuitive user interface

## Installation

### Requirements

- Python 3.10+
- conda (recommended) or pip

### Install Dependencies

```bash
# Using conda (recommended)
conda create -n pdf2word python=3.10
conda activate pdf2word
pip install -e .

# Or using uv
uv sync
```

## Usage

### 1. Start Backend Server

```bash
conda activate pdf2word
python backend/app.py
```

The server will start at `http://127.0.0.1:5000`.

### 2. Start Frontend Server

```bash
conda activate pdf2word
python -m http.server 8080 --directory frontend
```

### 3. Access the Application

Open `http://localhost:8080` in your browser.

### 4. Convert Files

1. Click the "Choose File" button to select a PDF file
2. Click the "Start Conversion" button
3. Watch the real-time conversion progress (current page/total pages + percentage)
4. After conversion, the file will automatically download

## Project Structure

```
pdf2word/
├── backend/
│   └── app.py              # Flask backend server
├── frontend/
│   └── index.html          # Frontend page
├── pyproject.toml          # Python dependencies
└── README.md              # Project documentation
```

## Tech Stack

### Backend
- **Flask**: Web framework
- **Flask-CORS**: CORS support
- **pdf2docx**: PDF to Word conversion library
- **SSE**: Server-Sent Events for real-time progress

### Frontend
- **HTML5**: Page structure
- **CSS3**: Styling
- **JavaScript (ES6+)**: Interactive logic, Fetch API + ReadableStream

## API Endpoints

### POST /convert-stream

SSE streaming conversion endpoint with real-time progress updates.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (PDF file)

**Response:**
- Content-Type: text/event-stream
- Event types:
  - `progress`: Progress update
  - `complete`: Conversion complete, contains download_id
  - `error`: Error message

**Progress Event Example:**
```json
{
  "stage": "parsing",
  "message": "Parsing... Page 5/10",
  "current": 5,
  "total": 10,
  "percent": 50
}
```

### GET /download/<download_id>

Download the converted file.

**Response:**
- Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
- Body: Word file content

### POST /convert

Synchronous conversion endpoint (kept for compatibility).

## FAQ

### Q: What if conversion is slow?
A: Conversion speed depends on the size and complexity of the PDF file. With real-time progress display, you can now clearly see the conversion progress.

### Q: What if the converted format is incorrect?
A: pdf2docx has limited support for some complex PDF formats. It's recommended to use PDF files with standard formatting.

### Q: How to change the port?
A: Modify the port number in `app.run(port=5000)` in `backend/app.py`.

### Q: Where is the downloaded file saved?
A: After conversion, the browser will show a save dialog where you can choose any location on your local disk.

## Contributing

Issues and Pull Requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pdf2docx](https://github.com/dothinking/pdf2docx) - PDF to Word conversion library
- [Flask](https://flask.palletsprojects.com/) - Web framework

## Contact

If you have any questions or suggestions, please submit an Issue.

---

**Note**: This tool is for learning and personal use only. Please do not use it for commercial purposes.