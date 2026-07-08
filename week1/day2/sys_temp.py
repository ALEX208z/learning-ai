import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key is not working")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
# prompt = "I love you baby!"
prompt = "Suggest a name for my food company"

# System
message_system={
    "role": "system",
    # "content": "You are my loving girlfriend"
    "content": "You are a brand manager who suggests a name for my food company, name should be in one word only"
}
message = {
    "role": role,
    # "prompt": role,  wrong
    "content": prompt
}

message = [message_system,message]
# Temperature by default is 0 meaning safe. range is [0,2]
response = client.chat.completions.create(model=model, messages=message, temperature=0.5)
# print(response)

answer = response.choices[0].message.content
print(answer)
