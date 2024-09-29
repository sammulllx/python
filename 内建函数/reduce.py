from functools import reduce

# 如果没有第一次的结果,就把第1和第2数据分别给x,y
print(reduce(lambda x, y: x+y, [1, 2, 3, 4]))
10

# 如果执行了额外的数据,例如本例子中的5,则把5当做第一次用的x
print(reduce(lambda x, y: x+y, [1, 2, 3, 4], 5))
15

print(reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd'))
'ddaabbcc'


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))
