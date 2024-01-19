import os
import random
from shutil import copy

def create_directory(path):
    """如果目录不存在，则创建新目录"""
    if not os.path.isdir(path):
        os.mkdir(path)

def data_set_split(src_data_folder, target_data_folder, slice_data=[0.4, 0.3, 0.3]):
    '''
    读取源数据文件夹，生成划分好的文件夹，分为train、val、test三个文件夹进行
    :param src_data_folder: 源数据文件夹路径
    :param target_data_folder: 目标文件夹路径
    :param slice_data: 划分数据比例 [训练, 验证, 测试]
    :return: None
    '''
    print("开始数据集划分")
    class_names = os.listdir(src_data_folder)

    # 创建目标目录下的train, val, test文件夹
    split_names = ['train', 'val', 'test']
    for split_name in split_names:
        split_path = os.path.join(target_data_folder, split_name)
        create_directory(split_path)
        for class_name in class_names:
            create_directory(os.path.join(split_path, class_name))

    # 遍历每个类别并进行数据划分
    for class_name in class_names:
        current_class_data_path = os.path.join(src_data_folder, class_name)
        current_all_data = os.listdir(current_class_data_path)
        current_data_length = len(current_all_data)
        random.shuffle(current_all_data)

        # 计算训练、验证、测试数据的截止索引
        train_stop_idx = int(current_data_length * slice_data[0])
        val_stop_idx = train_stop_idx + int(current_data_length * slice_data[1])

        train_count = val_count = test_count = 0

        # 分别复制到train, val, test文件夹
        for i, file_name in enumerate(current_all_data):
            src_img_path = os.path.join(current_class_data_path, file_name)
            if i < train_stop_idx:
                target_folder = os.path.join(target_data_folder, 'train', class_name)
                train_count += 1
            elif i < val_stop_idx:
                target_folder = os.path.join(target_data_folder, 'val', class_name)
                val_count += 1
            else:
                target_folder = os.path.join(target_data_folder, 'test', class_name)
                test_count += 1
            copy(src_img_path, target_folder)

        print(f"类别 {class_name} 按照 {slice_data[0]}：{slice_data[1]}：{slice_data[2]} 的比例划分完成，共 {current_data_length} 张图片")
        print(f"训练集 {train_count} 张, 验证集 {val_count} 张, 测试集 {test_count} 张")

if __name__ == '__main__':
    src_data_folder = r"/Users/zy/Desktop/cropped_images"
    target_data_folder = r"/Users/zy/Desktop/c"
    data_set_split(src_data_folder, target_data_folder, slice_data=[0.6, 0.2, 0.2])
