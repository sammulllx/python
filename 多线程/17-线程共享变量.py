'''
g_num和NUM一般表示全局变量
'''

from threading import Thread
import time

g_num = 100


def work1():
    global g_num  # 如果全局变量是列表,字典可以直接用不需要加global
    for i in range(3):
        g_num += 1

    print("----in work1, g_num is %d---" % g_num)


def work2():
    global g_num
    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---" % g_num)

t1 = Thread(target=work1)
t1.start()

# 延时一会，保证t1线程中的事情做完 如果不延迟,t1不一定比t2先执行
time.sleep(1)

t2 = Thread(target=work2)
t2.start()
