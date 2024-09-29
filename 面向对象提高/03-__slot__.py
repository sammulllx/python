class Person(object):
    __slots__ = ("name", "age")


class Test(Person):
    pass


P = Person()
P.name = "teacher"  # 可以执行
P.age = 20  # 可以执行
# P.score = 100  # 执行失败

t = Test()
t.score = 100
