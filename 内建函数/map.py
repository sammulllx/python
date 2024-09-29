# 使用 lambda 表达式，将列表中的每个元素进行平方操作，并将结果转换为列表赋值给变量 a
a = list(map(lambda x: x*x, [1, 2, 3]))

# 打印列表 a
print(a)

# 遍历列表 a 中的每个元素
for temp in a:
    # 打印当前遍历到的元素
    print(temp)


print('*'*30)
# 使用 lambda 表达式定义一个函数，将两个参数相加


# 将两个列表 [1, 2, 3] 和 [4, 5, 6] 对应元素相加得到新的列表 b
b = list(map(lambda x, y: (x, y), [1, 2, 3], (4, 5, 6)))
# 遍历列表 b，输出每个元素
for temp in b:
    print(temp)


print('*'*30)


def f1(x, y):
    return x, y


l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)
print(list(l3))
# 结果为:[(0, 'Sun'), (1, 'M'), (2, 'T'), (3, 'W'), (4, 'T'), (5, 'F'), (6, 'S')]

print('*'*30)

m = map(str, map(lambda x: x ** 2, range(1, 10)))
print(list(m))

n = map(lambda x: x**2, range(1, 10))
print(list(n))

str = 'abc'
print(list(str))
