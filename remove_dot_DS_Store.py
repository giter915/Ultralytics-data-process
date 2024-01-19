import os

file_path = '/Users/zy/Desktop/cropped_images/.DS_Store'

# 检查文件是否存在
if os.path.isfile(file_path):
    try:
        os.remove(file_path)
        print(f"文件 {file_path} 已被删除。")
    except Exception as e:
        print(f"删除文件时出错: {e}")
else:
    print(f"文件 {file_path} 不存在。")
