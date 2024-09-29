'''
py2中
range(stop) -> list of integers
range(start, stop[, step]) -> list of integers
1.	方括号 []：表示方括号里面的内容是可选的，也就是你可以提供这个参数，也可以不提供。
2.	逗号,：用于分隔函数参数。它说明即使 step 是可选的，它依然和前面的 start、stop 是分隔开的，并且具有固定的顺序。

Python2中range返回列表，Python3中range返回一个range对象，是一个可以迭代的对象，可以配合for或者next等使用

当然了如果想得到列表，可通过list函数
'''
from collections.abc import Iterable, Iterator


a = range(5)
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))


# 创建列表的两种方法
l1 = list(a)
l2 = [x+2 for x in range(5)]
print(l1)
print(l2)
