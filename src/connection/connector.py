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

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False
        )
        return response.choices[0].message.content

connector = Connector()
