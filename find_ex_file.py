import os

def list_files_without_extension(directory):
    """列出目录中所有文件名（不带后缀）"""
    files = os.listdir(directory)
    return {os.path.splitext(file)[0] for file in files}

def find_extra_files(dir1, dir2):
    """找到两个目录中多余的文件名"""
    files_dir1 = list_files_without_extension(dir1)
    files_dir2 = list_files_without_extension(dir2)

    # 找到只在 dir1 或 dir2 中存在的文件名
    extra_in_dir1 = files_dir1 - files_dir2
    extra_in_dir2 = files_dir2 - files_dir1

    return extra_in_dir1, extra_in_dir2

def delete_extra_files(directory, extra_files):
    """删除目录中多余的文件"""
    for file in extra_files:
        # 由于文件名不带后缀，我们需要找到匹配的文件并删除
        for filename in os.listdir(directory):
            if os.path.splitext(filename)[0] == file:
                file_path = os.path.join(directory, filename)
                os.remove(file_path)
                print(f"已删除文件: {file_path}")

if __name__ == "__main__":
    dir1 = "small_tip/labels"  # 替换为你的第一个目录路径
    dir2 = "small_tip/images"  # 替换为你的第二个目录路径

    extra_in_dir1, extra_in_dir2 = find_extra_files(dir1, dir2)

    print("在 dir1 中多余的文件名：")
    for file in extra_in_dir1:
        print(file)

    print("\n在 dir2 中多余的文件名：")
    for file in extra_in_dir2:
        print(file)

    # 删除多余的文件
    delete_extra_files(dir1, extra_in_dir1)
    delete_extra_files(dir2, extra_in_dir2)