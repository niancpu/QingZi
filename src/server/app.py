from fastapi import FastAPI
from src.server.routes import chat_router

app = FastAPI(title="QingZi - AI 数字人", version="1.0.0")

# 注册路由
app.include_router(chat_router)


@app.get("/")
def health():
    """健康检查"""
    return {"status": "running"}
