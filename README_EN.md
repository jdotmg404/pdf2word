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
- Node.js 18+ (for frontend development)

### Install Dependencies

```bash
# Backend dependencies
uv sync  # or pip install -e .

# Frontend dependencies
cd frontend && npm install
```

## Usage

### 1. Start Backend Server

```bash
python backend/app.py
```

The server will start at `http://127.0.0.1:5000`.

### 2. Start Frontend Server

```bash
cd frontend
npm run dev
```

The frontend development server will start at `http://localhost:5173`.

### 3. Access the Application

Open `http://localhost:5173` in your browser.

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
│   ├── src/
│   │   ├── App.vue         # Main application component
│   │   ├── main.ts         # Entry file
│   │   ├── components/     # Vue components
│   │   ├── composables/    # Composable functions
│   │   └── types/          # TypeScript type definitions
│   ├── package.json
│   └── vite.config.ts
├── pyproject.toml          # Python dependencies
└── README.md
```

## Tech Stack

### Backend
- **Flask**: Web framework
- **Flask-CORS**: CORS support
- **pdf2docx**: PDF to Word conversion library
- **SSE**: Server-Sent Events for real-time progress

### Frontend
- **Vue 3**: Progressive JavaScript framework
- **TypeScript**: Type safety
- **Vite**: Next-generation frontend build tool

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
A: Modify the backend port in `app.run(port=5000)` in `backend/app.py`; configure frontend port in `frontend/vite.config.ts`.

### Q: Where is the downloaded file saved?
A: After conversion, the browser will show a save dialog where you can choose any location on your local disk.

## Development

```bash
# Build frontend for production
cd frontend && npm run build

# Preview production build
cd frontend && npm run preview
```

## Contributing

Issues and Pull Requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pdf2docx](https://github.com/dothinking/pdf2docx) - PDF to Word conversion library
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Vue.js](https://vuejs.org/) - Frontend framework

## Contact

If you have any questions or suggestions, please submit an Issue.

---

**Note**: This tool is for learning and personal use only. Please do not use it for commercial purposes.