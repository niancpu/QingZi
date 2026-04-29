"""
LiteLLM 单轮调用示例
从 .env 文件加载 API 配置
"""

# 加载 .env 文件
load_dotenv()

# 从环境变量获取配置
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")

