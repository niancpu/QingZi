from pydantic import BaseModel


class ChatInput(BaseModel):
    user_input: str
    ai_said:str
    round_id:int
    chat_time:str

