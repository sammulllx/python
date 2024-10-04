import threading

mutex = threading.Lock()
mutex.acquire()
print('hhh')
mutex.acquire()
mutex.release()

'''
如果这个互斥锁已经被上锁了,那么在这个锁被解开之前,
是不能再次上锁的,也就是说:如果这个锁被上锁在解开之前
谁要是再次调用acquire对其上锁,那么谁就被被堵塞,直到
这个互斥锁被解锁为止
注意:一定是同一把锁才可以
'''
