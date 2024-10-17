class MyList(object):
    """自定义的一个可迭代对象"""

    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""

    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration("没了")
        # for 循环捕获到这个异常后，会自动停止循环，而不会显示异常信息。

    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    # 在 for num in mylist 中，print 打印的是 MyIterator 的 __next__ 返回的元素值，而不是 MyList 对象本身
    # for num in mylist:
    #     print(num)

    myiterator = iter(mylist)
    try:
        while True:
            print(next(myiterator))
    except StopIteration as e:
        print(f'Stopped: {e}')

    # iterator = iter(mylist)  # 手动获取迭代器
    # print(next(iterator))    # 输出 1
    # print(next(iterator))    # 输出 2
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))

    print('end')
