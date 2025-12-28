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
SYSTEM_PROMPT = "You are a helpful assitant that helps students, assuming that their prior knowledge is very basic. "
def ask_ai (prompt):
    import datetime
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
    with open("llm_inference_data.txt", "a",encoding="utf-8") as file:
      file.write("----- New Interaction -----\n")
      file.write(prompt + "\n")
      file.write(answer + "\n")
      file.write("--------------------------\n")
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
    print("Inference completed successfully. Check llm_inference_data.txt for details.")    
 