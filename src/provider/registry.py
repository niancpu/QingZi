from openai import OpenAI
import litellm
import os
from dotenv import load_dotenv
from litellm.exceptions import AuthenticationError, RateLimitError, APIError

class ProviderRegistry:
    def __init__(self):
        self._provider={}
    
    def register(self,name):
        def decorator(cls):
            self._provider[name]=cls
            return cls
        return decorator
    def get_SDK(self,provider):
        return self._provider if provider=="custom" else self._provider[provider]

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
class LiteLLM:
    def __init__(self,
                 api_key,
                 base_url,
                 model,
                 protocol="openai",
                 temperature=0.7,
                 **kwargs):
        self.api_key=api_key
        self.base_url=base_url
        self.protocol=protocol
        self.model=model
        self.temperature=temperature
    def send_message(self,messages):
        
        try:
                response = litellm.completion(
                    model=f"{self.protocol}/{self.model}",
                    messages=messages,
                    api_base=self.base_url,
                    temperature=self.temperature
                )
                
                content=response or ""
                if content is not None:
                    return content
                else:
                    return ""
                # return content or ""
        except AuthenticationError as e:
            print(f"Bad API key: {e}")
        except RateLimitError as e:
            print(f"Rate limited: {e}")
        except APIError as e:
                print(f"API error: {e}")


def sdk_router(provider):
    return llm_registry.get_SDK(provider)


