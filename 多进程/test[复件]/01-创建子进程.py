# from multiprocessing import Process
# import time


# def test():
#     """子进程单独执行的代码"""
#     while True:
#         print('---test---')
#         time.sleep(1)


# if __name__ == '__main__':
#     p = Process(target=test)
#     p.start()
#     # 主进程单独执行的代码
#     while True:
#         print('---main---')
#         time.sleep(1)
from multiprocessing import Process
import os
import time


def run_proc():
    """子进程要执行的代码"""
    print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
    print('子进程将要结束...')


if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()
