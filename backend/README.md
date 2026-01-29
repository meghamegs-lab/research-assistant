# Research Assistant Backend

FastAPI backend with AI agent capabilities.

## Setup

1. Install dependencies:
```bash
   pip install -r requirements.txt
```

2. Create `.env` file:
```bash
   cp .env.example .env
```

3. Add your API keys to `.env`:
```
   ANTHROPIC_API_KEY=your_key_here
```

4. Run the server:
```bash
   uvicorn main:app --reload
```

5. API will be available at `http://localhost:8000`
6. Interactive docs at `http://localhost:8000/docs`

## Endpoints

- `GET /` - Health check
- `POST /research` - Submit a research question
```

#### **Root .gitignore**
```
# Environment variables
*.env
.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
backend/venv/
backend/env/

# Node (if you add Node later)
node_modules/
npm-debug.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log