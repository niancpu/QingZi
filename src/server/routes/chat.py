from fastapi import APIRouter
from src.services import AIService

from base import ChatInput

router = APIRouter()
ai_service = AIService()


@router.post("/chat")
def chat(user_input: ChatInput):
    """处理聊天请求"""
    reply = ai_service.genera(user_input.user_input)
    return {"reply": reply}
