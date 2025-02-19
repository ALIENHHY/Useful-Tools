# 读取文件内容并删除重复行
def remove_duplicates(file_path):
    # 打开文件并读取所有行
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 使用集合去重，然后按原顺序重新排列
    unique_lines = list(dict.fromkeys(line.strip() for line in lines))

    # 将去重后的内容写回文件，每条唯一内容占一行
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in unique_lines:
            file.write(f"{line}\n")
    
    print(f"去重完成，最终内容已保存至 {file_path}。")

# 使用示例
file_path = "password.txt"
remove_duplicates(file_path)
