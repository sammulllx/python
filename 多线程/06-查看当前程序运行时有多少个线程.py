import threading
import time

print(threading.enumerate())


def task_1():
    for i in range(5):
        print('11111')
        time.sleep(1)


def task_2():
    for i in range(5):
        print('22222')
        time.sleep(1)


t1 = threading.Thread(target=task_1)  # 创建一个Thread的实例对象后,不会创建新的线程
print(threading.enumerate())
# t2 = threading.Thread(target = task_2)
t1.start()  # 调用实例对象的start方法后,才会创建新的子线程
print(threading.enumerate())
# t2.start()

time.sleep(6)
print(threading.enumerate())
