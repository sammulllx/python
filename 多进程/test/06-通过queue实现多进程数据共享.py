import multiprocessing
import time


def task1(q):
    for i in ['A', 'B', 'C']:
        q.put(i)


def task2(q):
    while True:
        time.sleep(0.5)
        if not q.empty():
            value = q.get()
            print("提取出来的数据是:", value)

        else:
            break


if __name__ == '__main__':
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=task1, args=(q,))
    p2 = multiprocessing.Process(target=task2, args=(q,))
    p1.start()
    p2.start()
    p1.join()  # 等待进程 p1 结束
    p2.join()  # 等待进程 p2 结束
# import multiprocessing
# import time


# def task1(q):
#     for i in ['A', 'B', 'C']:
#         q.put(i)


# def task2(q):  # 将队列作为参数传递给 task2
#     while True:
#         time.sleep(0.5)
#         if not q.empty():
#             value = q.get()
#             print("提取出来的数据是:", value)
#         else:
#             break


# if __name__ == '__main__':
#     q = multiprocessing.Queue()  # 创建队列
#     p1 = multiprocessing.Process(target=task1, args=(q,))
#     p2 = multiprocessing.Process(target=task2, args=(q,))  # 传递队列参数
#     p1.start()
#     p2.start()

#     p1.join()  # 等待进程 p1 结束
#     p2.join()  # 等待进程 p2 结束
