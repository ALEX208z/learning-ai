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
prompt="Do you know me"
message = {
    "role": role,
    # "prompt": role,  wrong
    "content": prompt
}

message = [message]

response=client.chat.completions.create(model=model, messages=message)
print(response)

answer=response.choices[0].message.content
print(answer)
