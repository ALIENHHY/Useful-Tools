from openai import OpenAI

client_GPT = OpenAI(
    base_url='[YOUR-BASE-URL]',
    api_key='[YOUR-API-KEY]'
)

def chat_with_gpt():
    print("你可以开始和我对话了。输入 '退出' 来结束对话。")
    while True:

        user_input = input("你: ")

        if user_input.lower() == "退出":
            print("对话结束，谢谢你的提问！")
            break

        completion = client_GPT.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        print("助手:", completion.choices[0].message)

chat_with_gpt()
