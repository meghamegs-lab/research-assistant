from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from anthropic import Anthropic
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the same directory as this file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI(title="Research Assistant API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

# Verify API key is loaded
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables!")

print(f"✅ Anthropic API Key loaded: {ANTHROPIC_API_KEY[:20]}...")

# Initialize Anthropic client directly
client = Anthropic(api_key=ANTHROPIC_API_KEY)

@app.get("/")
def read_root():
    import time
    return {
        "message": "Research Assistant API is running!",
        "status": "healthy",
        "model": "Claude 3 Haiku",
        "timestamp": time.time(),
        "api_key_loaded": bool(ANTHROPIC_API_KEY)
    }

@app.post("/research")
async def research(question: Question):
    try:
        print(f"📝 Received question: {question.question}")

        # Use Anthropic SDK directly
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=[{"role": "user", "content": question.question}]
        )

        answer = message.content[0].text
        print(f"✅ Claude response received")

        return {
            "answer": answer,
            "sources": [
                {"title": "Claude 3 Haiku", "url": "#"}
            ]
        }
    except Exception as e:
        import traceback
        print(f"❌ Error: {str(e)}")
        print(f"❌ Traceback: {traceback.format_exc()}")
        return {
            "answer": f"I encountered an error: {str(e)}",
            "sources": []
        }

@app.get("/health")
def health_check():
    return {"status": "healthy", "model": "Claude 3 Haiku"}