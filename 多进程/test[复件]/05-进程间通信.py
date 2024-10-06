from multiprocessing import Queue

q = Queue(3)

q.put("消息1")
q.put("消息2")
print(q.full())  # False

q.put("消息3")
print(q.full())  # True

# 因为消息列队已满,所以会导致下面的try都会抛出异常
# 第一个try会等待2秒后再抛出异常
# 第二个Try会立刻抛出异常

# try:
#     q.put('message4', timeout=2)
# except Exception:
#     print('queue is full,now message num :%s' % q.qsize())

# try:
#     q.put_nowait('message4')
# except Exception:
#     print('queue is full,now message num:%s' % q.qsize())

if not q.full():
    q.put_nowait('message4')
# macos中无法使用 q.qsize()，直接通过遍历来获取队列内容
if not q.empty():
    while not q.empty():
        print(q.get_nowait())
