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

# 3 prompts
prompt1 = "Hi!"
prompt2 = "Explain time travel in detail in under 100 words!"
prompt3 = "Write a 1000 word essay on Machine learning!"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = [{"role": role, "content": prompt}]

    response = client.chat.completions.create(model=model, messages=message)

    answer = response.choices[0].message.content
    usage = response.usage

    print(f"Prompt: {prompt}")
    # print(f"Response: {answer}")
    print(f"Tokens -> prompt: {usage.prompt_tokens}, completion: {usage.completion_tokens}, total: {usage.total_tokens}")
    # print(f"finish reason : {response.choices[0].finish_reason}")
    print("-" * 80)