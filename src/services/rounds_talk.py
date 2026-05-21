from pathlib import Path
import threading
from typing import TYPE_CHECKING
from datetime import datetime

from dao import json_oper
from config import paths

_lock=threading.Lock()
#定义一个排他锁

class TalkHistory:
    def __init__(self):
        self._time_name=datetime.now().strftime("%Y%m%d_%H%M%S")
        self._path:Path=paths.get_home_path()/self._time_name

    if TYPE_CHECKING:
        from server.routes.base import ChatInput

    def save_talk(self,chat_input:'ChatInput',reply:str)->None:
        delta=json_oper.json_loader(self._path)
        with _lock: 
            json_oper.json_check_writer(self._path,delta)
    
    def read_talk(self)->dict:
        data:dict=json_oper.json_loader(self._path)
        return data
history=TalkHistory()


