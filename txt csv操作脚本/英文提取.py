import re

# 读取1.txt文件内容（确保文件编码为UTF-8）
with open('1.txt', 'r', encoding='utf-8') as infile:
    content = infile.read()

# 使用正则表达式匹配所有形如 "name": "XXX" 的模式，并提取XXX部分
# 这里的正则表达式解释：
#   \"name\":   匹配 "name": 字符串
#   \s*         匹配任意空白字符（0个或多个）
#   \"([^"]+)\" 匹配双引号内的内容，其中([^"]+)表示匹配除双引号外的一个或多个字符，并作为一个分组提取
matches = re.findall(r'"name":\s*"([^"]+)"', content)

# 将提取出的单词用空格连接
result = '; '.join(matches)

# 将结果写入2.txt文件中
with open('2.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(result)

print("提取完成，结果已存入 2.txt")
