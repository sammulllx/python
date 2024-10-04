import threading
import time


def print_lines(num):
    for i in range(num):
        print('11111')
        time.sleep(0.1)


def print_lines2(num1, num2):
    for i in range(num1):
        print('2222')
        time.sleep(0.1)
    for i in range(num2):
        print('3333')
        time.sleep(0.1)


def work2(num1, num2, num3, n):
    print("----in work1--num1=%d,num2=%d,num3=%d,n=%d" %
          (num1, num2, num3, n))
    # n是关键字参数


# t = threading.Thread(target=print_lines, args=(2,))  # 创建对象
# t2 = threading.Thread(target=print_lines2, args=(3, 4))
# t.start()
# t2.start()


t3 = threading.Thread(target=work2, args=(
    11, 22), kwargs={'n': 44, 'num3': 33})
t3.start()  # 真正创建线程

# t3 = threading.Thread(None, work2, args=(
#     11, 22), kwargs={'n': 44, 'num3': 33})
# t3.start()
