#!/usr/bin/env python3
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

key = os.getenv('ANTHROPIC_API_KEY')
print(f"API Key: {key[:20]}... (length: {len(key)})")

# Test with anthropic SDK directly
from anthropic import Anthropic

client = Anthropic(api_key=key)
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=50,
    messages=[{"role": "user", "content": "Say hello"}]
)

print(f"Success! Response: {message.content[0].text}")
