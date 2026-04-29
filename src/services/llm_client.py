"""
LiteLLM 单轮调用示例
从 .env 文件加载 API 配置
"""
from litellm import completion
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 从环境变量获取配置
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")

assert api_key is not None

# 设置 API 密钥
os.environ["OPENAI_API_KEY"] = api_key

# 单轮调用示例
response = completion(
    model=f"openai/{model}",
    messages=[{"role": "user", "content": "你好，请介绍一下你自己"}],
    api_base=base_url,
)

print(response.choices[0].message.content)#type:ignore