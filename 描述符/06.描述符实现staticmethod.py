class classmethod_new(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(self.func, instance, owner)

        # return self.func #此方法不能实现
        # return self.func(owner) #这是不可以的
        def call(*args):
            self.func(owner, *args)
        return call


class A(object):
    M = 100

    def a(self):
        print("----a 是实例方法 ----")

    @classmethod_new
    def b(cls):
        print("----b是类方法1----")
        print(cls.M)
        print("----b是类方法2----")

    @classmethod_new
    def c(cls, num1, num2):
        print("----c是类方法----")
        print(cls.M + num1 + num2)
        print("----c是类方法----")


obj = A()
obj.b()
# obj.c(1, 2)

# print('-'*50)

# A.b()
# A.c(3, 4)
