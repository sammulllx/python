def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def add_end(L=[]):
    L.append('END')
    return L


def add_end_pro(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(power(5, 2))
print(power(5))

enroll('sam', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')  # 不按顺序赋值

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print(add_end())
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

print(add_end_pro())
print(add_end_pro())
print(add_end_pro())
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
