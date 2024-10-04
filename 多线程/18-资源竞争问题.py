'''
g_num+=1分为:
1.获取g_num的值
2.+1得到一个新的值
3.修改g_num中的值

'''
from threading import Thread


g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        g_num += 1

    print("----in work1, g_num is %d---" % g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1

    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---" % g_num)

t1 = Thread(target=work1, args=(1000000,))
t1.start()


t2 = Thread(target=work2, args=(1000000,))
t2.start()
