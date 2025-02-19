from langchain_community.chat_models import ChatOllama

ollama_llm = ChatOllama(model="deepseek-r1:latest")

def chat_with_gpt():
    print("你可以开始和我对话了。输入 '退出' 来结束对话。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == "退出":
            print("对话结束，谢谢你的提问！")
            break
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
        chat_model_response = ollama_llm.invoke(messages)
        print("助手:", chat_model_response)

chat_with_gpt()
