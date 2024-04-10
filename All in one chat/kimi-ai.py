from openai import OpenAI
from flask import Flask, request,jsonify
 
client = OpenAI(
    api_key="sk-hV0GFR7b8CIY8qDAxezLL9NZbJPZHzq10G0oZuu9HHNC9byj",
    base_url="https://api.moonshot.cn/v1",
)
 
completion = client.chat.completions.create(
  model="moonshot-v1-8k",
  messages=[
    {"role": "system", "content": "you only speak english"},
    {"role": "user", "content": "hello"}
  ],
  temperature=0.3,
)
 
print(completion.choices[0].message.content)