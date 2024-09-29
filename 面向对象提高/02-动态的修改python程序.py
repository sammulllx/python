import types


# 定义了一个类
class Person(object):
    num = 0

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("---默认的实例方法---")


# 定义一个实例方法
def run(self, speed):
    print("----实例方法--1--")
    print("%s在移动, 速度是 %d km/h" % (self.name, speed))
    print("----实例方法--2--")


# 定义一个类方法
@classmethod
def test_class(cls):
    print("----类方法--1--")
    print("num=%d" % cls.num)
    cls.num = 100
    print("num=%d" % cls.num)
    print("----类方法--2--")

# 定义一个静态方法


@staticmethod
def test_static():
    print("----静态方法--1--")
    print("---static method----")
    print("----静态方法--2--")


# 创建一个实例对象
p = Person("老王", 24)
# 调用在class中的方法
p.eat()

# 给这个对象添加实例方法
p.run = types.MethodType(run, p)
# 调用实例方法
p.run(180)

# 除了实例方法麻烦点,其他都是直接等于就完事

# 给Person类绑定类方法
Person.test_class = test_class

# 调用类方法
Person.test_class()

# 给Person类绑定静态方法
Person.test_static = test_static
# 调用静态方法
Person.test_static()
