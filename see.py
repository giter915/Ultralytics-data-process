import os
from lxml import etree

def extract_categories(xml_directory):
    categories = set()
    for filename in os.listdir(xml_directory):
        if filename.endswith('.xml'):
            xml_path = os.path.join(xml_directory, filename)
            tree = etree.parse(xml_path)
            for element in tree.findall('.//object/name'):
                categories.add(element.text)
    return categories

# 设置包含XML文件的目录
xml_directory = '/Users/zy/Desktop/Dian/xmls'

# 提取类别
categories = extract_categories(xml_directory)

# 打印类别
print("找到的类别:")
for category in categories:
    print(category)
