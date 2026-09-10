"""
写一个用来遍历某目录所有内容的函数

"""
import os

# 1. 遍历某目录下的所有文件和文件夹
# 2. 判断是文件or文件夹
# 3. 如果是文件直接打印，如果是文件夹就再次判断，直到没有文件夹为止

def print_content(dir):
    for path in os.listdir(dir):
        full_path = os.path.join(dir, path)
        if os.path.isdir(full_path):
            print_content(full_path)
        else:
            print(full_path)

print_content("../")

"""
"""