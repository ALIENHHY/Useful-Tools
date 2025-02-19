import csv

def remove_duplicates_csv(file_path):
    # 读取CSV文件内容
    with open(file_path, 'r', encoding='ISO-8859-1', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # 使用集合去重，考虑所有列内容
    unique_rows = []
    seen = set()
    for row in rows:
        row_tuple = tuple(row)  # 将每行转换为元组以便进行哈希操作
        if row_tuple not in seen:
            unique_rows.append(row)
            seen.add(row_tuple)
    
    # 将去重后的内容写回文件
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(unique_rows)
    
    print(f"去重完成，最终内容已保存至 {file_path}。")

# 使用示例
file_path = "train.csv"
remove_duplicates_csv(file_path)
