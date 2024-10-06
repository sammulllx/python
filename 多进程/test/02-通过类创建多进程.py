from multiprocessing import Process
import time


class MyNewProcess(Process):
    def run(self):
        while True:
            print('---1---')
            time.sleep(1)


if __name__ == '__mian__':
    p = MyNewProcess()
    # 调用p.start()方法，p会先去父类中寻找start()，然后在Process的start方法中调用run方法
    p.start()

    while True:
        print('---Main---')
        time.sleep(1)
