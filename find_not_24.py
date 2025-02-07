import os
def delete_files(file_list):
    """删除文件列表中的所有文件"""
    for file_path in file_list:
        os.remove(file_path)
        print(f"已删除文件: {file_path}")
def check_file_lines(directory):
    """检查目录中所有txt文件的行数，找到不是24行的文件"""
    invalid_files = []  # 存储不符合条件的文件路径

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # 只处理txt文件
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if len(lines) > 96:  # 检查行数是否为24
                    invalid_files.append(file_path)

    return invalid_files

if __name__ == "__main__":
    directory = "small_tip/labels"  # 替换为你的目录路径
    invalid_files = check_file_lines(directory)

    if invalid_files:
        print("以下文件的不是24行数据：")
        for file in invalid_files:
            print(file)
        delete_files(invalid_files)

    else:
        print("所有txt文件都是24行数据。")