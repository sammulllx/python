import copy
a = [11]
b = (a,)
c = [b]

# d = copy.copy(c)
# print(id(c), id(d))
# a.append(22)
# print(c)
# print(d)

# 如果是copy.deepcopy,那么一定是递归拷贝,即全部复制
d = copy.deepcopy(c)
print(id(c), id(d))
a.append(22)
print(c)
print(d)
