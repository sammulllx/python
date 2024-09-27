

import time


class FibIterator(object):
    """斐波那契数列迭代器"""

    def __init__(self):
        # num1用来保存前前一个数，初始值为数列中的第一个数1
        self.num1 = 1
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        temp_num = self.num1
        self.num1, self.num2 = self.num2, self.num1+self.num2
        return temp_num

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self


fib = FibIterator()
x = iter(fib)

# 因为fib是迭代器所以不必使用iter()函数，直接使用next()函数即可
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for xxx in fib:
    print(xxx)
    time.sleep(1)
