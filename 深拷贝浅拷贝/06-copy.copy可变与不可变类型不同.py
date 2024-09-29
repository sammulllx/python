import copy
a = [11, 22, 33]
b = (11, 22, 33)  # 不可变类型, 仅仅是引用复制,相当于d=b

c = copy.copy(a)
d = copy.copy(b)
# 当使用copy.copy来完成浅拷贝的时候,它其实需要检测一下 拷贝的数据类型是否可变,
# 如果是则浅拷贝(拷贝最顶层),否则复制引用

print(id(a), id(c))
print(id(b), id(d))
