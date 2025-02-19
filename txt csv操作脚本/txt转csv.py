import csv

# 读取txt文件并去除空行
def read_txt_and_remove_empty_lines(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
        
    # 去除空行并返回
    clean_lines = [line.strip() for line in lines if line.strip()]
    return clean_lines

# 将内容写入CSV文件
def write_to_csv(csv_file_path, data):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow([line])

# 主函数
def main():
    txt_file_path = 'input.txt'  # 替换为你的txt文件路径
    csv_file_path = 'output.csv'  # 输出的CSV文件路径
    
    # 读取txt并清理空行
    clean_data = read_txt_and_remove_empty_lines(txt_file_path)
    
    # 写入CSV
    write_to_csv(csv_file_path, clean_data)
    print(f"数据已成功写入 {csv_file_path}")

# 调用主函数
if __name__ == '__main__':
    main()
