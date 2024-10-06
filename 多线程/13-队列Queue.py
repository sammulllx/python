import queue

q = queue.Queue()
q.put('11')  # 存入字符串
q.put(22)  # 存入整数
q.put({'num': 100})  # 存入字典

print(q.get())  # 11
print(q.get())  # 22
print(q.get())  # {'num': 100}


# get没有的值的时候会等待
