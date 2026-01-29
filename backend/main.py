from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import Tool
from langchain.agents.agent import AgentExecutor
from langchain.agents import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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

# Initialize Claude LLM
llm = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    anthropic_api_key=ANTHROPIC_API_KEY,
    temperature=0.2
)

# Create a simple knowledge tool (no web search needed for now)
def knowledge_base(query: str) -> str:
    """Answers questions using Claude's knowledge"""
    return f"Using my knowledge to answer: {query}"

# Create tool
knowledge_tool = Tool(
    name="Knowledge",
    func=knowledge_base,
    description="Use your built-in knowledge to answer questions"
)

# Agent prompt template
template = """Answer the following question as best you can using your knowledge.

Question: {input}

Think through this step by step and provide a helpful answer.

{agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)

# Create the agent
tools = [knowledge_tool]
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=3
)

@app.get("/")
def read_root():
    return {
        "message": "Research Assistant API is running!",
        "status": "healthy",
        "model": "Claude 3.5 Sonnet"
    }

@app.post("/research")
async def research(question: Question):
    try:
        print(f"📝 Received question: {question.question}")
        
        # Use direct LLM call (simpler and more reliable)
        messages = [HumanMessage(content=question.question)]
        response = llm.invoke(messages)
        
        print(f"✅ Claude response received")
        
        return {
            "answer": response.content,
            "sources": [
                {"title": "Claude AI", "url": "#"}
            ]
        }
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {
            "answer": f"I encountered an error: {str(e)}",
            "sources": []
        }

@app.get("/health")
def health_check():
    return {"status": "healthy", "model": "Claude 3.5 Sonnet"}