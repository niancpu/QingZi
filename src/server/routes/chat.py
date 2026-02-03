from fastapi import APIRouter
from pydantic import BaseModel
from src.services import AIService

router = APIRouter()
ai_service = AIService()


class ChatInput(BaseModel):
    user_input: str


@router.post("/chat")
def chat(user_input: ChatInput):
    """处理聊天请求"""
    reply = ai_service.generate_reply(user_input.user_input)
    return {"reply": reply}
