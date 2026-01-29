# Research Assistant Frontend

Simple HTML/CSS/JavaScript frontend for the AI Research Assistant.

## Setup

1. Open `index.html` in a browser
2. Or use a local server:
```bash
   python -m http.server 3000
```
3. Navigate to `http://localhost:3000`

## Configuration

Update the `API_URL` in `script.js` to point to your backend:
```javascript
const API_URL = 'http://localhost:8000'; // Local development
// const API_URL = 'https://your-backend-url.com'; // Production
```