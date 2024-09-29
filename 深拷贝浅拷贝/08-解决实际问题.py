import os
import copy


def count_file(files):
    """
    测试列表中，非隐藏文件的个数
    :param files:
    :return:
    """
    # 4. 使用列表推导式生成一个不包含隐藏文件的新列表
    files = [file for file in files if not file.startswith(".")]

    # 5. 排序打印测试
    files.sort()
    for file in files:
        print(file)


# 1. 遍历出当前文件夹中所有的文件
file_names = os.listdir(".")

print("-" * 30)

# 2. 打印所有的文件名
for file in file_names:
    print(file)

print("-" * 30)

# 2. 调用一个函数，用来测试除了隐藏文件之外的文件的个数
count_file(copy.deepcopy(file_names))  # 深拷贝，避免修改原文件列表

print("-" * 30)

# 3. 打印所有的文件名，确保原文件名列表未修改
for file in file_names:
    print(file)
