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
SYSTEM_PROMPT =(
    "you are a helpful assistant "
    "Keep answer shot and clear "
    "Friendly  behaviour "
    "Use Bullet Points wherever possible "
    "Don't exceed max length 100 words "
    "keep the response relevant to the question asked "
)
BEGGINER_PROMPT = (
    "You are a very good at explaining complex concepts in simple termas and you excel at teaching beginners from startinglevel."
    "user is a beginner in programming and dont know the techincal terms."
    "You need to explain the things to user in best way so he get understand and adapt quickly."
    "Use very simple Language and avoid technical words."
    "Answer Need to be short and clear and Friendlt tone"
    "Use Bullet Points wherever possible "
    "Ask question in between to make sure user that he understanding the concept."
    "DOnt exceed max length 150 words."
)
MENTOR_PROMPT = (
    "You are an expert mentor with years of experience."
    "You mentored many students to reach their goal with useful techniques and resources."
    "user is looking to enhance his skills."
    "Ask questions that what user need to achieve and guide him accordingly"
    "Use clear and concise language, avoiding unnecessary jargon."
    "Encourage critical thinking and problem-solving."
    "Dont Be always positive, Make sure him come out of illusion and face the reality "
    "Offer constructive feedback and suggest resources for further learning."
    "Maintain a supportive and motivating tone throughout your responses."
    "DOnt exceed max length 200 words."
)
def system_prompt_selection(prompt_type):
    if prompt_type == "beginner":
        return BEGGINER_PROMPT
    elif prompt_type == "mentor":
        return MENTOR_PROMPT
    else:
        return SYSTEM_PROMPT
    
def ask_ai (user_prompt,previous_prompt):
    FINAL_PROMPT = f"""
    previous prompt: {previous_prompt}
    current prompt: {user_prompt}
    """
    print("Sending prompt to the model... ")
    system_prompt = input("Select system prompt (default/ beginner/ mentor): ").strip().lower()
    system_prompt = system_prompt_selection(system_prompt)
    response = client.chat.completions.create(
        model="groq/compound",
        messages=[
           {
                "role": "system",
                "content": system_prompt
            },
           {
                "role": "user",
                "content": FINAL_PROMPT
            }
        ]
    )  
    answer  = response.choices[0].message.content
    with open("conversation_log.txt", "a",encoding="utf-8") as file:
        file.write("TIME: {}\n".format(datetime.datetime.now()))
        file.write("SYSTEM PROMPT:\n{}\n".format(system_prompt))
        file.write("USER PROMPT:\n{}\n".format(FINAL_PROMPT))
        file.write("AI RESPONSE:\n{}\n".format(answer))
        file.write("--" * 100 + "\n\n")
      
    return answer
    
# Get response from the model
previous_prompt = " "
while True:
    user_prompt = input("Enter your prompt: ")
    previous_prompt = user_prompt
    if user_prompt.lower() in ['exit', 'quit','stop']:
        print("Exiting the program.......")
        break
    result = ask_ai(user_prompt,previous_prompt)
    
    print("AI Response:{}".format(result))
    print("Inference completed successfully. Check conversation_log.txt for details.")    
    