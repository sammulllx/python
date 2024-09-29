import copy

a = [11, 22]
b = [33, 44]
c = [a, b]

d = copy.deepcopy(c)

a.append(55)

print(c)
print(d)

print(id(c[0]))
print(id(d[0]))
