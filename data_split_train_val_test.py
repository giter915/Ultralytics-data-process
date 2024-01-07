import os
import random
from tqdm import tqdm

#指定images文件夹路径
image_dir = '/Users/zy/project1/dataset-processing-format/coco128-seg/images/train2017'
#指定labels文件夹路径
label_dir = '/Users/zy/project1/dataset-processing-format/coco128-seg/labels/train2017'

#创建一个空列表来存储有效图片的路径
valid_images = []
#创建一个空列表来存储有效labels的路径
valid_labels = []

#遍历images文件夹下的所有图片
for image_name in os.listdir(image_dir):
    #获取图片的完整路径
    image_path = os.path.join(image_dir,image_name)
    #获取图片文件的扩展名
    ext = os.path.splitext(image_path)[-1]
    #根据扩展名替换成对应的label文件名
    label_name = image_name.replace(ext,'.txt')
    print(label_name)
    #获取对应label的完整路径
    label_path = os.path.join(label_dir,label_name)
    #判断label是否存在
    if not os.path.exists(label_path):
        #删除图片
        os.remove(image_path)
        print('deleted:',image_path)
    else:
        #将图片路径添加到列表中
        valid_images.append(image_path)
        # 将label路径添加到列表中
        valid_labels.append(label_path)
        # print('valid:',image_path,label_path)

#遍历每个有效图片路径
for i in tqdm(range(len(valid_images))):
    image_path = valid_images[i]
    label_path = valid_labels[i]
    #随机生成一个概率
    r = random.random()
    #判断图片应该移动到那个文件件
    #train valid test
    if r < 0.1:
        destiation = '/Users/zy/project1/dataset-processing-format/coco128-seg-voc/test'
    elif r < 0.2:
        destiation = '/Users/zy/project1/dataset-processing-format/coco128-seg-voc/valid'
    else:
        destiation = '/Users/zy/project1/dataset-processing-format/coco128-seg-voc/trian'

    #生成目标文件夹中图片的新路径
    image_destination_path  = os.path.join(destiation,'images',os.path.basename(image_path))
    #移动图片到目标文件夹
    os.rename(image_path,image_destination_path)
    #生成目标文件夹中label新路径
    label_destination_path = os.path.join(destiation,'labels',os.path.basename(label_path))
    # 移动图label到目标文件夹
    os.rename(label_path, label_destination_path)

print('valid images:', valid_images)
print('valid labels:', valid_labels)
