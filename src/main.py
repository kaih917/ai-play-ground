from connection.connector import Connector
from token_component.deepseek_tokenizer import DeepSeekTokenizer
from contest.chat_contest import ChatContest

if __name__ == "__main__":
    connector = Connector()

    test_system_prompt = "You are a teacher who is good at explaining things in a simple way."
    test_prompt = ["What is the capital of France?", "What is the popuplation of this city?"]

    chat_contest = ChatContest(test_system_prompt)
    for prompt in test_prompt:
        chat_contest.appender(prompt)

    tokenizer = DeepSeekTokenizer()
    print("Token estimate:", tokenizer.token_estimate(chat_contest.contest))

    response = connector.chat(chat_contest.contest)
    print(response)


    # print(connector.chat([
    #     {"role": "system", "content": "You are a helpful assistant"},
    #     {"role": "user", "content": "Hello"},
    #     {"role": "user", "content": "What is the capital of France?"},
    # ]))

    # tokenizer = DeepSeekTokenizer()
    # print(tokenizer.encode("Hello!"))