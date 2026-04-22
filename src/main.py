from connection.connector import Connector
from token_component.deepseek_tokenizer import DeepSeekTokenizer

if __name__ == "__main__":
    connector = Connector()
    print(connector.chat([
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ]))

    tokenizer = DeepSeekTokenizer()
    print(tokenizer.encode("Hello!"))