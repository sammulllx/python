# 1.导入threading模块
# 2.使用threading模块中的thread创建一个对象
# 3.调用这个实例对象的start方法
import time
import threading


def task_1():
    for i in range(5):
        print('任务A   ', i)  # 11111和22222的先后顺序随机,看个人操作系统
        time.sleep(0.2)


def task_2():
    for i in range(5):
        print('任务B   ', i)  # 11111和22222的先后顺序随机,看个人操作系统
        time.sleep(0.2)


t1 = threading.Thread(target=task_1)  # 创建了一个实例对象 task_1是函数引用

t2 = threading.Thread(target=task_2)  # 创建了一个实例对象 task_1是函数引用
t1.start()  # t1不一定比t2先执行

t2.start()

# 任务A    0
# 任务B    0
# 任务B    1
# 任务A    1
# 任务B    2
# 任务A    2
# 任务B    3
# 任务A    3
# 任务B    4
# 任务A    4


# 任务A    0
# 任务B    0
# 任务A    1
# 任务B    1
# 任务A    2
# 任务B    2
# 任务A    3
# 任务B    3
# 任务A    4
# 任务B    4
