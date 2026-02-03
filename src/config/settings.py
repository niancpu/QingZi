import os
from dotenv import load_dotenv

load_dotenv()

# AI API 配置
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

# 服务器配置
SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")
SERVER_PORT = int(os.getenv("SERVER_PORT", "8000"))

# 验证必要配置
if not API_KEY:
    raise RuntimeError("AI API_KEY 未配置")
if not BASE_URL:
    raise RuntimeError("AI BASE_URL 未配置")
if not MODEL:
    raise RuntimeError("AI MODEL 未配置")
