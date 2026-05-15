import os
import requests
import json
from dotenv import load_dotenv
from pypdf import PdfReader
import gradio as gr
from openai import OpenAI

load_dotenv(override=True)

def push(text):
    requests.post(
        os.getenv("PUSH_URL"),
        data={
            "token": os.getenv("PUSH_API_KEY"),
            "user": os.getenv("PUSH_USER"),
            "message": text,
        }
    )

openai = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1")

messages = [{"role": "user", "content": "What is 2+2?"}]
response = openai.chat.completions.create(
    model=os.getenv("GPT"),
    messages=messages,
)
print(response.choices[0].message.content)