import os
import numpy as np
import cv2

# 修改输入图片文件夹
img_folder = "images/"
label_folder = "labels/"  # 修改输入标签文件夹
output_folder = os.path.join(os.getcwd(), "output")  # 输出图片文件夹位置

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 类别颜色映射
colormap = {
    0: (0, 255, 0),  # 类别0: 绿色
    1: (132, 112, 255),  # 类别1: 紫色
    2: (0, 191, 255)  # 类别2: 蓝色
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


if __name__ == '__main__':
    img_list = sorted(os.listdir(img_folder))
    label_list = sorted(os.listdir(label_folder))

    for img_name, label_name in zip(img_list, label_list):
        image_path = os.path.join(img_folder, img_name)
        label_path = os.path.join(label_folder, label_name)

        try:
            # 读取图像文件
            img = cv2.imread(image_path)
            if img is None:
                raise FileNotFoundError(f"无法读取图像文件: {image_path}")

            h, w = img.shape[:2]

            # 读取 labels
            with open(label_path, 'r') as f:
                lb = np.array([x.split() for x in f.read().strip().splitlines()], dtype=np.float32)

            # 绘制每一个目标
            for x in lb:
                img = xywh2xyxy(x, w, h, img)

            # 保存结果图
            output_path = os.path.join(output_folder, f"{os.path.splitext(img_name)[0]}.png")
            cv2.imwrite(output_path, img)

        except Exception as e:
            print(f"处理文件 {img_name} 时出错: {e}")