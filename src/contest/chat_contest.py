class ChatContest:
    def __init__(self, system_prompt="You are a helpful assistant"):
        self.contest = []
        self.contest.append({"role": "system", "content": system_prompt})

    def appender(self, user_input):
        self.contest.append({"role": "user", "content": user_input})
        print(f"User input is added: {user_input}")
