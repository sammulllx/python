import gevent
import random
import time
from gevent import monkey


monkey.patch_all()


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


def coroutine_work2(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


gevent.joinall([
    gevent.spawn(coroutine_work, "work1"),
    gevent.spawn(coroutine_work2, "work2")
])
