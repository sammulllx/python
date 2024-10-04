'''
注意点1:
当线程task1、task2执行的时候,双方要抢着给mutex这个互斥锁上锁
不管是哪个线程先抢到,都会保证一件事情:其它的线程会卡在上锁的那个位置
例如: task1先对mutex上锁,会导致在调用release解锁之前,task2线程会堵塞在
mutex.acquire上锁的那个位置,一直到 task1线程调用了mutex.release()释放锁

当task1调用了release释放锁之后,接下来task1与task2线程依然会抢着给mutex上锁
不确定会让哪个线程上锁,这是操作系统做的事情,我们程序不能控制

注意点2
如果在task1与task2折2个线程都抢着上锁的时候,恰巧task1线程抢到了999999次
当下一次的时候task2抢到了500000次,再下一次的时候taask1抢到了,此时
task1总共执行的100万次已经完成,而此时打印出来的g_num的值是150万,而不是100万


'''
from threading import Thread, Lock

mutex = Lock()


g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in work1, g_num is %d---" % g_num)


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---" % g_num)

t1 = Thread(target=work1, args=(1000000,))
t1.start()


t2 = Thread(target=work2, args=(1000000,))
t2.start()
