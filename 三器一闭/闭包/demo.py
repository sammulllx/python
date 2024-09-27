a = [1, 2]
b = 3


def f():
    a[0] = 100
    b = 300


f()
print(a)
print(b)
