# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from config import BasicConfig

os.environ["OPENAI_API_KEY"] = BasicConfig.API_TOKEN

class Connector:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=BasicConfig.API_URL)

    def chat(self, messages, thinking_mode=False, thinking_degree=1):
        try:
            if thinking_mode:
                if thinking_degree == 1:
                    reasoning_effort="low"
                else:
                    reasoning_effort="high"
                
                response = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages,
                    stream=False,
                    extra_body={"thinking": {"type": "enabled"}},
                    reasoning_effort=reasoning_effort
                )
            else:
                response = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages,
                    stream=False,
                    extra_body={"thinking": {"type": "disabled"}}
                )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error occurred: {e}")
            return "An error occurred while processing your request."

connector = Connector()
