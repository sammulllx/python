import multiprocessing
import os


def main():
    folder_name = input("请输入要复制的文件夹名字")
    file_names = os.listdir(folder_name)
    print(file_names)


if __name__ == '__main__':
    main()
