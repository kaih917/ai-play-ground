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
    
    def token_estimate(self, chart_contest):
        total_tokens = 0
        for message in chart_contest:
            total_tokens += len(self.tokenizer.encode(message["content"]))
        return total_tokens

tokenizer = DeepSeekTokenizer()