# QingZi - AI 数字人

一个基于 FastAPI 的 AI 数字人聊天项目。

## 项目结构

```
QingZi/
├── .env.example          # 环境变量示例
├── .gitignore
├── README.md
├── requirements.txt      # 项目依赖
├── run_server.py         # 服务器启动入口
├── run_client.py         # 客户端启动入口
│
└── src/                  # 源代码目录
    ├── config/           # 配置模块
    │   └── settings.py
    ├── server/           # 服务器模块
    │   ├── app.py
    │   └── routes/
    │       └── chat.py
    ├── services/         # 业务逻辑层
    │   └── ai_service.py
    └── client/           # 客户端模块
        └── cli.py
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 并填写配置：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```
API_KEY=your_api_key_here
BASE_URL=https://api.openai.com/v1
MODEL=gpt-3.5-turbo
SERVER_HOST=127.0.0.1
SERVER_PORT=8000
```

### 3. 启动服务器

```bash
python run_server.py
```

### 4. 启动客户端

```bash
python run_client.py
```

## API 接口

### 健康检查

```
GET /
```

### 聊天

```
POST /chat
Content-Type: application/json

{
    "user_input": "你好"
}
```

## 许可证

MIT
