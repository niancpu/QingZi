from typing import Union
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from config import API_KEY,BASE_URL,MODEL
import uvicorn  
from uuid import uuid4
from collections import defaultdict

app=FastAPI()

client=OpenAI(
    api_key=API_KEY,

    base_url=BASE_URL,
)

assert MODEL is not None,"model未配置"

class Input(BaseModel):
    user_input:str 

@app.get("/")
def health():
    return {"status":"running"}

@app.post("/chat")
def chat(user_input:Input):
    reply=generate_reply(user_input.user_input)
    return {"reply":reply}
def generate_reply(user_text:str,systemPrompt="你是一个友好、自然的中文数字人助手，名字叫晴子。不要使用表情包，使用可爱的颜文字"
):
    if "你好" in user_text or "hello" in user_text:
        return "Ciallo ～(∠・ω< )⌒★!"
    elif (
    "你是谁" in user_text
    or "你的名字是什么" in user_text
    or "你叫什么名字" in user_text
):

        return "我的名字叫晴子，是一个ai数字人捏"
    try:
        completion=client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role":"system","content":systemPrompt},
                {"role":"user","content":user_text}
            ],
            max_tokens=1024,
            temperature=0.7

        )
        return completion.choices[0].message.content or ""
    except Exception as e:
        raise  RuntimeError(f"API请求失败：{e}")from e
