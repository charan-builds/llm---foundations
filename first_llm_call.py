"""
NOTE:
This file uses OpenRouter API (OpenAI-compatible).
Using free / low-cost models for learning.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Read OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")

# Create OpenAI client with OpenRouter base URL
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Make a simple request
response = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct:free",
    messages=[
        {
            "role": "user",
            "content": "Explain Python dictionaries in very simple words."
        }
    ],
)

# Print response (ALWAYS index 0)
print(response.choices[0].message.content)
