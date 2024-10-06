import multiprocessing
import os
import random
import time


def copy_file(q, name, folder_name, dest_folder_name):
    time.sleep(random.randint(0, 1))
    with open(folder_name+'/'+name, 'rb') as f:
        content = f.read()
    with open(dest_folder_name+'/'+name, 'wb') as f:
        f.write(content)
    q.put(name)


def main():
    folder_name = input("请输入要复制的文件夹名字")
    dest_folder_name = folder_name + '[复件]'
    file_names = os.listdir(folder_name)
    try:
        os.mkdir(dest_folder_name)
    except Exception:
        pass
    print(file_names)

    q = multiprocessing.Manager().Queue()

    pool = multiprocessing.Pool(3)
    for name in file_names:
        pool.apply_async(copy_file, (q, name, folder_name, dest_folder_name))

    for i in range(len(file_names)):
        file_name = q.get()
        print('\r当前的进度是:%.2f%%,已经复制完成的文件名是:%s%s'
              % ((i+1)/len(file_names)*100, file_name, ' '*30), end='')
    print()
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
