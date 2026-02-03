from openai import OpenAI
from src.config import API_KEY, BASE_URL, MODEL


class AIService:
    """AI 对话服务"""

    DEFAULT_SYSTEM_PROMPT = "你是一个友好、自然的中文数字人助手，名字叫晴子。不要使用表情包，使用可爱的颜文字"

    def __init__(self):
        self.client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
        self.model: str = MODEL  # type: ignore

    def generate_reply(self, user_text: str, system_prompt: str | None = None) -> str:
        """生成 AI 回复"""
        if system_prompt is None:
            system_prompt = self.DEFAULT_SYSTEM_PROMPT

        # 预设回复
        if "你好" in user_text or "hello" in user_text.lower():
            return "Ciallo ～(∠・ω< )⌒★!"
        elif any(
            keyword in user_text
            for keyword in ["你是谁", "你的名字是什么", "你叫什么名字"]
        ):
            return "我的名字叫晴子，是一个ai数字人捏"

        # 调用 AI API
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_text},
                ],
                max_tokens=1024,
                temperature=0.7,
            )
            return completion.choices[0].message.content or ""
        except Exception as e:
            raise RuntimeError(f"API请求失败：{e}") from e


# 单例实例
ai_service = AIService()
