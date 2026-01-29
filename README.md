# AI Research Assistant

A simple web app that uses AI agents to research questions and provide answers.

## Project Structure
```
research-assistant/
├── frontend/          # HTML/CSS/JavaScript frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
└── backend/           # FastAPI Python backend
    ├── main.py
    ├── requirements.txt
    └── .env
```

## Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
python -m http.server 3000
# Or just open index.html in your browser
```

Visit `http://localhost:3000`

## Features

- 🤖 AI-powered research assistant
- 🔍 Web search capabilities
- 💬 Clean chat interface
- 🚀 Simple and beginner-friendly

## Technologies

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI
- **AI**: Anthropic Claude API

## License

MIT