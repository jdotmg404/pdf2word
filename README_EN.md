# PDF to Word Converter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-green.svg)](https://www.python.org/downloads/)

A simple and easy-to-use online PDF to Word conversion tool with custom save location support.

## Features

- 🚀 **Fast Conversion**: Based on pdf2docx library for efficient PDF conversion
- 💾 **Custom Save Location**: Choose any local disk location to save converted files
- 🌐 **Cross-platform**: Supports Windows, Linux, macOS
- 🎨 **Clean Interface**: Simple and intuitive user interface

## Screenshot

![Conversion Interface](screenshot.png)

## Installation

### Requirements

- Python 3.7+
- pip or conda

### Install Dependencies

```bash
# Using pip
pip install -r requirements.txt

# Using conda
conda create -n pdf2word python=3.8
conda activate pdf2word
pip install -r requirements.txt
```

## Usage

### 1. Start Backend Server

```bash
python backend/app.py
```

The server will start at `http://127.0.0.1:5000`.

### 2. Start Frontend Server

```bash
# Method 1: Using Python HTTP Server
python -m http.server 8080 --directory frontend

# Method 2: Open index.html directly
# Open frontend/index.html in your browser
```

### 3. Access the Application

Open `http://localhost:8080` in your browser.

### 4. Convert Files

1. Click the "Choose File" button to select a PDF file
2. Click the "Start Conversion" button
3. Wait for conversion to complete
4. After conversion, the file will automatically download
5. Choose the save location in the browser's save dialog

## Project Structure

```
pdf2word/
├── backend/
│   └── app.py              # Flask backend server
├── frontend/
│   └── index.html          # Frontend page
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Tech Stack

### Backend
- **Flask**: Web framework
- **Flask-CORS**: CORS support
- **pdf2docx**: PDF to Word conversion library

### Frontend
- **HTML5**: Page structure
- **CSS3**: Styling
- **JavaScript (ES6+)**: Interactive logic

## API Endpoints

### POST /convert
Upload PDF file and start conversion, returns the converted Word file.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (PDF file)

**Response:**
- Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
- Body: Word file content

## FAQ

### Q: What if conversion is slow?
A: Conversion speed depends on the size and complexity of the PDF file. It's recommended to test with smaller files.

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
