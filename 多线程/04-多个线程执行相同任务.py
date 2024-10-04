import time
import threading


def say_sorry():
    for i in range(5):
        print('I am so sorry')
        time.sleep(1)


t1 = threading.Thread(target=say_sorry)
t2 = threading.Thread(target=say_sorry)
t1.start()
t2.start()
# 主线程虽然执行完了代码,但是主线程等待子线程执行结束后,才结束
