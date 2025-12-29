"""
NOTE:
This file uses OpenRouter API (OpenAI-compatible).
Using free / low-cost models for learning.
"""

import os
import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Read Groq API key
api_key = os.getenv("Groq_API_KEY")
if not api_key:
     raise ValueError("Groq_API_KEY not found in environment variables.") 

# Create OpenAI client with Groq base URL
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Make a simple request 
SYSTEM_PROMPT = " you are a helpful assistant. User is a beginner in programming. Keep answer shortand clear.Friendly and mentor like behaviour and Use Bullet Points. Expalin like I am new .Don't exceed max length 100 words. Avoid Technical words."
def ask_ai (prompt):
    
    print("Sending prompt to the model... ")
    response = client.chat.completions.create(
        model="groq/compound",
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
    with open("Prompt_check.md", "a",encoding="utf-8") as file:
      file.write("------------------------------- New Interaction ----------------------------------------------------\n")
      file.write("Prompt given to the model:{}\n".format(SYSTEM_PROMPT))
      file.write(prompt + "\n")
      file.write(answer + "\n")
      file.write("----------------------------------------------------------------------------------------------------\n")
      file.write("Time: {}\n".format(datetime.datetime.now()))
    return answer
    
# Get response from the model
while True:
    user_prompt = input("Enter your prompt: ")
    if user_prompt.lower() in ['exit', 'quit','stop']:
        print("Exiting the program.......")
        break
    result = ask_ai(user_prompt)
    print("AI Response:{}".format(result))
    print("Inference completed successfully. Check Prompt_check.md for details.")    
 