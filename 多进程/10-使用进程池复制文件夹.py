import multiprocessing
import os


def copy_file(name, folder_name, dest_folder_name):
    with open(folder_name+'/'+name, 'rb') as f:
        content = f.read()
    with open(dest_folder_name+'/'+name, 'wb') as f:
        f.write(content)


def main():
    folder_name = input("请输入要复制的文件夹名字")
    dest_folder_name = folder_name + '[复件]'
    file_names = os.listdir(folder_name)
    os.mkdir(dest_folder_name)
    print(file_names)

    pool = multiprocessing.Pool(3)
    for name in file_names:
        pool.apply_async(copy_file, (name, folder_name, dest_folder_name))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
