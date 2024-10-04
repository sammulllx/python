# 1.导入threading模块
# 2.使用threading模块中的thread创建一个对象
# 3.调用这个实例对象的start方法
import time
import threading


def task_1():
    while True:
        print('11111')  # 11111和22222的先后顺序随机,看个人操作系统
        time.sleep(1)


t1 = threading.Thread(target=task_1)  # 创建了一个实例对象 task_1是函数引用
t1.start()

while True:
    print('22222')
    time.sleep(1)
