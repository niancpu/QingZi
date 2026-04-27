import json
from pathlib import Path
def json_loader(json_path:Path,)->dict:
    try:
        with open(json_path,"r",encoding='UTF-8') as f:
            data=json.load(f)
            return data
    except (FileNotFoundError,json.JSONDecodeError,Exception) as e:
        raise RuntimeError(f"文件{json_path}打开错误:{type(e).__name__},{e}") from e
   
def json_check_writer(json_path:Path,delta:dict)->None:
    if not json_path.exists():
        json_path.touch()       
    if json_path.stat().st_size>0:            
        try:
            with open(json_path,"r",encoding='UTF-8') as f:
                data=json.load(f)
        except (FileNotFoundError,json.JSONDecodeError) as e:
            raise RuntimeError(f"文件{json_path}打开错误:{type(e).__name__},{e}") from e
        #type(e).__name__获取异常的名称
        delta=data|delta
    try:
        with open(json_path,"w",encoding='UTF-8') as f:
            json.dump(delta,f,ensure_ascii=False,indent=4)
    except (FileNotFoundError,json.JSONDecodeError) as e:
        raise RuntimeError(f"文件{json_path}打开错误:{type(e).__name__},{e}") from e

