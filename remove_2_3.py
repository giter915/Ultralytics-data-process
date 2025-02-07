import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue

        # 处理第一列
        first_col = parts[0]
        if first_col == '2':
            parts[0] = '0'
        elif first_col == '3':
            parts[0] = '1'
        else:
            continue  # 如果不是2也不是3，跳过这一行

        new_lines.append(' '.join(parts) + '\n')

    # 将处理后的内容写回文件
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            process_file(file_path)

# 替换为你的目录路径
directory_path = 'big_tip_labels'
process_directory(directory_path)