from openai import OpenAI
from src.config import API_KEY, BASE_URL, MODEL


class AIService:
    """AI 对话服务"""

    DEFAULT_SYSTEM_PROMPT = "你是一个友好、自然的中文数字人助手，名字叫晴子。不要使用表情包，使用可爱的颜文字"

    def __init__(self):
       self.client=OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
       )
    def loop(self,
             spliced_messages:list
             
             ):


# 单例实例
ai_service = AIService()
