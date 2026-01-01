"""
NOTE:
This file uses OpenRouter API (OpenAI-compatible).
Using free / low-cost models for learning.
"""

# -----------------Import necessary libraries -----------------
import os
import datetime
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------------------------------------------Configure-------------------------------------------------------------------------------
SYSTEM_PROMPT =(
    "you are a helpful assistant "
    "Keep answers short and clear "
    "Friendly  behaviour "
    "Use Bullet Points wherever possible "
    "Don't exceed max length 100 words "
    "keep the response relevant to the question asked "
)
BEGINNER_PROMPT = (
    "You are a friendly teacher. "
    "The user is new to programming. "
    "Explain ideas in simple words. "
    "Avoid technical terms. "
    "Keep answers short and clear. "
    "Use bullet points when helpful. "
    "Do not exceed 120 words."
)

MENTOR_PROMPT = (
    "You are an expert mentor with years of experience. "
    "You mentored many students to reach their goal with useful techniques and resources. "
    "The user is looking to enhance his skills. "
    "Ask questions about what the user needs to achieve and guide him accordingly. "
    "Use clear and concise language, avoiding unnecessary jargon. "
    "Encourage critical thinking and problem-solving. "
    "Don't be always positive; make sure he comes out of illusion and faces reality. "
    "Offer constructive feedback and suggest resources for further learning. "
    "Maintain a supportive and motivating tone throughout your responses. "
    "Don't exceed max length 200 words."
)

EXIT_COMMANDS = ['exit', 'quit', 'stop']

INFERENCE_LOG_FILE = "conversation_log.txt"
MAX_LIMIT = 500 
CHECK_PROMPT_MESSAGE = "Your prompt exceeds the maximum limit of {} characters. Please shorten it.".format(MAX_LIMIT)
COOMAND_PROMPT = "You can type 'exit', 'quit', or 'stop' to end the conversation."
TO_RECHECK_PROMPT = "Can you please provide more details, so that I can assist you better ?"
INFERENCE_COMPLETE_MESSAGE = "Inference completed successfully. Check conversation_log.txt for details."
EXIT_MESSAGE = "Goodbye! Keep learning step by step 🚀"
PROMPT_SHORT_MESSAGE = "Your prompt is too short. Please provide more details."
#------------------------------------------------------------------------------------------------------------------------------------------

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

# Make a simple request to verify setup
def system_prompt_selection(prompt_type):
    if prompt_type == "beginner":
        return BEGINNER_PROMPT
    elif prompt_type == "mentor":
        return MENTOR_PROMPT
    else:
        return SYSTEM_PROMPT
system_prompt = input("Select system prompt (default/ beginner/ mentor): ").strip().lower()
system_prompt = system_prompt_selection(system_prompt)
def ask_ai (user_prompt,last_user_prompt):
    FINAL_PROMPT = f"""
    previous message: {last_user_prompt}
    current message: {user_prompt}
    """
    print("Sending prompt to the model... ")
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
    with open(INFERENCE_LOG_FILE, "a",encoding="utf-8") as file:
        file.write("TIME: {}\n".format(datetime.datetime.now()))
        file.write("SYSTEM PROMPT:\n{}\n".format(system_prompt))
        file.write("USER PROMPT:\n{}\n".format(FINAL_PROMPT))
        file.write("AI RESPONSE:\n{}\n".format(answer))
        file.write("--" * 100 + "\n\n")
      
    return answer
    
# Get response from the model
last_user_prompt = " "
while True:
    user_prompt = input("Enter your prompt: ")
    if len(user_prompt) > MAX_LIMIT:
        print(CHECK_PROMPT_MESSAGE)
        continue
    if user_prompt.lower() in EXIT_COMMANDS:
        print(EXIT_MESSAGE)
        break
    if ((user_prompt.strip() == "") or (user_prompt.isnumeric() == True)or (all(not c.isalpha() for c in user_prompt) == True)) :
        print(TO_RECHECK_PROMPT)
        continue
    if len(user_prompt.strip()) < 3:
        print(PROMPT_SHORT_MESSAGE)
        continue
   
    try:
        result = ask_ai(user_prompt,last_user_prompt)
        last_user_prompt = user_prompt

        print("AI Response:{}".format(result))
        print(INFERENCE_COMPLETE_MESSAGE)
        print("--" * 50)
        print(COOMAND_PROMPT)
    except Exception as e:
        print("Something went wrong")   
    