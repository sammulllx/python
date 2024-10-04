# from time import sleep
# import threading


# def sing():
#     for i in range(3):
#         print("singing...%d" % i)
#         sleep(1)


# def dance():
#     for i in range(3):
#         print("dancing...%d" % i)
#         sleep(1)


# if __name__ == '__main__':
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()

import threading
import time


def say_sorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(3)


for i in range(5):
    t = threading.Thread(target=say_sorry)
    t.start()  # 启动线程，即让线程开始执行

print(threading.enumerate())
