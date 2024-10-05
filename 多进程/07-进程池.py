from multiprocessing import Pool
import os
import random
import time


def worker(num):
    for i in range(5):
        print('===pid=%d==num=%d=' % (os.getpid(), num))
        time.sleep(1)


if __name__ == '__main__':
    # 3表示进程池中最多有三个进程一起执行
    pool = Pool(3)

    for i in range(10):
        print('---%d---' % i)
        # 向进程中添加任务
        # 注意：如果添加的任务数量超过了进程池中进程的个数的话，那么就不会接着往进程池中添加，
        #       如果还没有执行的话，他会等待前面的进程结束，然后在往
        # 进程池中添加新进程
        pool.apply_async(worker, (i,))

    pool.close()  # 关闭进程池 只是意味着不会再向进程池添加,但是进程池中可能该有进程在执行
    pool.join()  # 主进程在这里等待，只有子进程全部结束之后，在会开启主线程
