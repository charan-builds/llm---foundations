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
if not api_key:
    print("Error: OpenRouter API key is not working properly.")

# Create OpenAI client with OpenRouter base URL
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Make a simple request 
SYSTEM_PROMPT = "You are a helpful assitant that helps students assuming that their prior knowledge is very basic."
def ask_ai (prompt):
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[
           {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
           {
                "role": "user",
                "content":prompt
            }
        ]
    )  
    answer  = response.choices[0].message.content
    with open("log.txt", "a") as file:
      file.write("----- New Interaction -----\n")
      file.write(prompt + "\n")
      file.write(answer + "\n")
      file.write("--------------------------\n")
    print(answer)
    return "AI Responsed succesfully."
# Get response from the model
user_prompt = input("Enter your prompt: ")
result = ask_ai(user_prompt)
print("AI Response:{}".format(result))
