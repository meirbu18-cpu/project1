# pip install anthropic

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system="You are a concise technical assistant. Answer in one sentence, using plain language.",
    messages=[
        {"role": "user", "content": "What is a large language model?"}
    ]
)

print(message.content[0].text)
