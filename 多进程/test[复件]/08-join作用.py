import multiprocessing
import time


def task():
    for i in range(5):
        print("hahahah")
        time.sleep(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=task)
    p.start()
    print("----1----")
    p.join()  # 主进程等待子进程结束,释放执行结束的子进程资源,防止僵尸进程
    print("----2----")

    while True:
        print("xxxxxxxxx")
        time.sleep(1)
