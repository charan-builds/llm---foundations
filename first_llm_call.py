"""
NOTE:
#This file uses the OpenAI API.
# Currently blocked  due to no API credits.
 
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Make a simple request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Explain Python dictionaries in very simple words."}
    ]
)

# Print response
print(response.choices[0].message.content)


"""
NOTE:
#This file uses the OpenAI API.
# Currently blocked  due to no API credits.
 
"""