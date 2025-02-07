import os
import numpy as np
import cv2

# 输入文件夹路径
img_folder = "big_tip_images/"  # 原图文件夹
label_folder = "big_tip_labels/"  # 标签文件夹
output_folder = os.path.join(os.getcwd(), "big_tip_output_double")  # 输出文件夹

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 类别颜色映射
colormap = {
    0: (0, 255, 0),  # 类别0: 绿色
    1: (132, 112, 255),  # 类别1: 红色
    2: (0, 191, 255) , # 类别2: 蓝色
    3: (35, 25, 255)  # 类别2: 蓝色
}


# 坐标转换
def xywh2xyxy(x, w1, h1, img):
    label, x, y, w, h = x
    # 边界框反归一化
    x_t = x * w1
    y_t = y * h1
    w_t = w * w1
    h_t = h * h1
    # 计算坐标
    top_left_x = int(x_t - w_t / 2)
    top_left_y = int(y_t - h_t / 2)
    bottom_right_x = int(x_t + w_t / 2)
    bottom_right_y = int(y_t + h_t / 2)

    # 根据类别选择颜色
    color = colormap.get(int(label), (0, 0, 0))  # 默认黑色
    # 绘制矩形框
    cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), color, 2)
    return img


def concatenate_images(img1, img2):
    """将两张图片水平拼接"""
    return cv2.hconcat([img1, img2])


if __name__ == '__main__':
    img_list = sorted(os.listdir(img_folder))
    label_list = sorted(os.listdir(label_folder))

    for img_name, label_name in zip(img_list, label_list):
        image_path = os.path.join(img_folder, img_name)
        label_path = os.path.join(label_folder, label_name)

        try:
            # 读取原图
            img = cv2.imread(image_path)
            if img is None:
                raise FileNotFoundError(f"无法读取图像文件: {image_path}")

            h, w = img.shape[:2]

            # 读取 labels
            with open(label_path, 'r') as f:
                lb = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)

            # 绘制每一个目标
            visualized_img = img.copy()  # 复制原图用于可视化
            for x in lb:
                visualized_img = xywh2xyxy(x, w, h, visualized_img)

            # 将原图和可视化图拼接
            concatenated_img = concatenate_images(img, visualized_img)

            # 保存拼接后的图片
            # output_path = os.path.join(output_folder, f"{os.path.splitext(img_name)[0]}_concat.png")
            output_path = os.path.join(output_folder, f"{os.path.splitext(img_name)[0]}.png")
            cv2.imwrite(output_path, concatenated_img)
            print(f"已保存: {output_path}")

        except Exception as e:
            print(f"处理文件 {img_name} 时出错: {e}")