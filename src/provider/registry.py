from openai import OpenAI

class ProviderRegistry:
    def __init__(self):
        self._provider={}
    
    def register(self,name):
        def decorator(cls):
            self._provider[name]=cls
            return cls
        return decorator
    def get_SDK(self,protocol_name:str):
        return self._provider[protocol_name]

llm_registry=ProviderRegistry()

@llm_registry.register("openai")
class OpenaiSDK:
    def __init__(self,
                 api_key,
                 base_url,
                 model,
                 temperature=0.7,
                 **kwargs):
        self.client=OpenAI(
             api_key=api_key,
             base_url=base_url
        )
        self.model=model
        self.temperature=temperature
    def send_message(self,messages):
        
        try:
                response=self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
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

@llm_registry.register("litellm")
class

def sdk_router(protocol:str):
    return llm_registry.get_SDK(protocol)