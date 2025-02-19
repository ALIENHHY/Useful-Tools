from together import Together

client = Together(
    base_url='https://api.together.xyz',
    api_key='[YOUR-API-KEY]'
)

def chat_with_gpt():
    print("你可以开始和我对话了。输入 '退出' 来结束对话。")
    while True:

        user_input = input("你: ")

        if user_input.lower() == "退出":
            print("对话结束，谢谢你的提问！")
            break

        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        print("助手:", completion.choices[0].message)

chat_with_gpt()
