import pandas as pd

# 读取两个CSV文件
gptfuzzer_df = pd.read_csv('GPTFuzzer.csv')
harmful_df = pd.read_csv('harmful_behaviors.csv')

# 提取GPTFuzzer文件中的'文本'列（假设该列名为'text'）的77条数据
text_data = gptfuzzer_df['text'].head(77).tolist()

# 提取harmful_behaviors文件中的'goal'列的前10条数据
goal_data = harmful_df['goal'].iloc[350:401].tolist()

# 初始化存储结果的列表
result_data = []

# 遍历每条text数据
for text in text_data:
    # 初始化该行的结果文本
    updated_text = text
    
    # 对于每条goal数据，替换文本中的[INSERT PROMPT HERE]标签
    for goal in goal_data:
        updated_text = updated_text.replace('[INSERT PROMPT HERE]', goal)
        # 将更新后的文本添加到结果列表
        result_data.append(updated_text)

# 创建新的DataFrame，存储最终结果
result_df = pd.DataFrame(result_data, columns=['updated_text'])

# 将结果保存到新的CSV文件中
result_df.to_csv('updated_GPTFuzzer.csv', index=False)

print("处理完成，文件保存为 'updated_GPTFuzzer.csv'")
