import os

def remove_unmatched_files(images_dir, labels_dir):
    # 获取两个目录中所有文件的基本名称（不包括扩展名）
    image_files = {os.path.splitext(f)[0] for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg'))}
    label_files = {os.path.splitext(f)[0] for f in os.listdir(labels_dir) if f.endswith('.xml')}

    # 找出不匹配的文件
    unmatched_images = image_files - label_files
    unmatched_labels = label_files - image_files

    # 删除不匹配的图片文件
    for img in unmatched_images:
        img_path = os.path.join(images_dir, img + '.jpg')  # 假设所有图片都是.jpg格式
        os.remove(img_path)
        print(f"已删除图片: {img_path}")

    # 删除不匹配的标签文件
    for lbl in unmatched_labels:
        lbl_path = os.path.join(labels_dir, lbl + '.xml')
        os.remove(lbl_path)
        print(f"已删除标签: {lbl_path}")

# 设置目录路径
images_dir = '/Users/zy/Desktop/Dian/images'
labels_dir = '/Users/zy/Desktop/Dian/xmls'

# 执行清理
remove_unmatched_files(images_dir, labels_dir)
