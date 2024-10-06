import gevent
import time
from gevent import monkey


monkey.patch_all()  # 这句话一定要放到 使用time等耗时操作的前面，它最后的的效果是 将time模块中的延时全部替换为 gevent中的演示
# time模块中的延时是不具备 自动切换任务的功能，而gevent中的延时 具备，因此我们需要将time全部改为gevent，
# 为了更快速的让本.py中的所有time变为gevent所以我们需要执行 monkey.patch_all()


def f1(n):
    for i in range(n):
        print("-----f1-----", i)
        # gevent.sleep(1)
        time.sleep(1)


def f2(n):
    for i in range(n):
        print("-----f2-----", i)
        # gevent.sleep(1)
        time.sleep(1)


def f3(n):
    for i in range(n):
        print("-----f3-----", i)
        # gevent.sleep(1)
        time.sleep(1)


g1 = gevent.spawn(f1, 5)
g2 = gevent.spawn(f2, 5)
g3 = gevent.spawn(f3, 5)
g1.join()  # join会等待g1标识的那个任务执行完毕之后 对其进行清理工作，其实这就是一个 耗时操作
g2.join()
g3.join()

# 使用gevent来实现多任务的时候，有一个很特殊的地方
# 它可以自行切换协程指定的任务，而且切换的前提是：当一个任务用到耗时操作（例如延时），它就会把这个时间拿出来去做另外的任务
# 这样做最终实现了多任务 而且自动切换
