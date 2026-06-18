# pip install openai python-dotenv

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

completion = client.chat.completions.create(
    model="anthropic/claude-opus-4",
    messages=[
        {"role": "system", "content": "You are a concise technical assistant. Answer in one sentence, using plain language."},
        {"role": "user", "content": "What is a large language model?"}
    ]
)

print(completion.choices[0].message.content)
