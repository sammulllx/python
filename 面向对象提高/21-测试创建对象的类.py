# 测试数字的类
age = 35
print(age.__class__)


# 测试字符串的类
name = 'bob'
print(name.__class__)


# 测试函数的类
def Foo():
    pass


print(Foo.__class__)


# 测试实例对象的的类
class Bar(object):
    pass


b = Bar()
print(b.__class__)


# 测试类的类
class Bar(object):
    pass


print(Bar.__class__)
print("------分割线-------")

# 测试类型的类
print(age.__class__.__class__)
print(name.__class__.__class__)
print(Foo.__class__.__class__)
print(b.__class__.__class__)
print(Bar.__class__.__class__)  # type类的元类是type。。。。
