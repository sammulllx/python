import queue

q = queue.PriorityQueue()
q.put((10, 'Q'))
q.put((30, 'Z'))
q.put((20, 'A'))

print(q.get())  # (10, 'Q') #数字小优先级高
print(q.get())  # (20, 'A')
print(q.get())  # (30, 'Z')
