import gc


class ClassA():
    def __init__(self) -> None:
        print('object born,id:%s' % str(id(self)))


def f2():
    while True:  # 循环引用
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        gc.collect()  # 手动调用垃圾回收功能,这样子自动垃圾回收被关闭的情况下,也会进行回收


gc.disable()

f2()

'''
执行f2(),进程占用的内存会不断增大。
创建了c1,c2后这两块内存的引用计数都是1,执行c1.t=c2和c2.t=cl后,这两块内存的引用计数变成2.
在del c1后,引用计数变为1,由于不是为0,所以c1对象不会被销毁;同理,c2对象的引用数也是1。
python默认是开启垃圾回收功能的,但是由于以上程序已经将其关闭,因此导致垃圾回收器都不会回收它们,所以就会导致内存泄露
'''
