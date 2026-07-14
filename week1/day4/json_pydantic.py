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

# structure it
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema=Ticket.model_json_schema()
print(schema)

response_format={
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give me a json output.
{schema}
"""

message_system={
    "role": "system",
    "content": system_prompt
}

text = "Hello, My name is Ayush, I bought a Iphone from your store, it has stopped working, I am from Kolkata. my email is abc@gmail.com"
prompt=f"""
This is a customer ticket. Please extract the personal information from this
{text}
"""
message = {
    "role": role,
    # "prompt": role,  wrong
    "content": prompt
}

message = [message_system,message]

response=client.chat.completions.create(model=model, messages=message, response_format=response_format)
# print(response)

answer=response.choices[0].message.content
print(answer)



#how to read
import json 
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
