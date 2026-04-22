# pip3 install transformers
# python3 deepseek_tokenizer.py
import transformers
import os

class DeepSeekTokenizer:
    def __init__(self, tokenizer_dir="./"):
        print(os.path.dirname(os.path.abspath(tokenizer_dir)))
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(
            tokenizer_dir, trust_remote_code=True
        )

    def encode(self, text):
        return self.tokenizer.encode(text)

tokenizer = DeepSeekTokenizer()