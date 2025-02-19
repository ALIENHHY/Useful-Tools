import re

# 打开并读取 1.txt 文件内容（确保文件编码为 UTF-8）
with open('1.txt', 'r', encoding='utf-8') as infile:
    text = infile.read()

# 使用正则表达式提取所有连续的中文字符
# 这里使用 Unicode 范围 \u4e00-\u9fff 来匹配常用汉字
chinese_segments = re.findall(r'[\u4e00-\u9fff]+', text)

# 将每组中文用空格连接
result = ' '.join(chinese_segments)

# 将结果写入 2.txt 文件中（使用 UTF-8 编码）
with open('2.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(result)

print("提取完成，结果已存入 2.txt")
