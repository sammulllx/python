a = [11, 22]
b = [33, 44]

c = [a, b]
d = c[:]  # 当使用列表切片的时候,就是浅拷贝,与d=copy.copy(c)一样

print(c)
print(d)

print(id(c))
print(id(d))


a.append(55)

print(c)
print(d)
