from pathlib import Path
from dao import json_oper
import logging

_home_path=Path.home()/".qingzi_bot"

def set_path(path)->Path:
    try:
        Path(path).mkdir(parents=True,exist_ok=True)
        return path
    except Exception as e:
        raise RuntimeError(f"创建文件夹错误：{e}") from e

def get_home_path()-> Path:
    if _home_path.exists():
        return _home_path
    return set_path(_home_path)

def init_dir():
    try:
        set_path(_home_path/"history")
        json_oper.json_creater(_home_path/"config.json")
    except RuntimeError as e:
        logging.error(e)
