import threading
import time


class Task(threading.Thread):

    def run(self):
        while True:
            print(self.name)
            print('1111')
            time.sleep(1)
            self.xxx()  # 必须自己在run方法中自己调用

    def xxx(self):
        pass


t = Task()
t.start()  # 调用父类中的start方法,start会自动调用run


while True:
    print('main')
    time.sleep(1)
