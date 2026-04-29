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
    def loop(self,spliced_messages:list)
        
    def generate_reply(self, spliced_messages:list) -> str:
        """生成 AI 回复"""
        assert MODEL is not None,"Model can't be None"

        if system_prompt is not None:
            system_prompt=self.DEFAULT_SYSTEM_PROMPT

        from services import fixed_reply        
        
        try:
            response=self.client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role":"system","content":self.DEFAULT_SYSTEM_PROMPT},
                    {"role":"user","content":user_text}
                ],
                stream=False
            )
            
            content=response.choices[0].message.content
            if content is not None:
                return content
            else:
                return ""
            # return content or ""
        except Exception as e:
            raise RuntimeError(f"API请求错误:{e}") from e


# 单例实例
ai_service = AIService()
