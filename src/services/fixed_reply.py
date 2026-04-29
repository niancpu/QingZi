
def reply(user_text:str):
    if "你好" in user_text or "hello" in user_text.lower():
            return "Ciallo ～(∠・ω< )⌒★!"
    elif any(
            keyword in user_text
            for keyword in ["你是谁", "你的名字是什么", "你叫什么名字"]
        ):
            return "我的名字叫晴子，是一个ai数字人捏"