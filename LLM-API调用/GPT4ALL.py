from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
with model.chat_session():
    while True:
        print("下面开始对话：")
        user_input = input("你: ")
        if user_input.lower() in ["退出", "exit", "quit"]:
            print("再见！")
            break
        response = model.generate(user_input, max_tokens=256)
        print(f"GPT4All: {response}")