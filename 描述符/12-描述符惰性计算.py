'''
惰性计算:一定是要得到一个值,这个值是需要一个计算得来的而不是提前准备好的,
在什么时候真正需要的时候 什么时候才计算,而不是一调用就立马计算
'''


class LazyProperty(object):
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        print("---LazyProperty__get_---")
        if instance is None:
            return self
        value = self.fun(instance)  # 50.24
        setattr(instance, self.fun.__name__, value)
        return value


class ReadonlyNumber(object):
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("%s is not modifiable" % self.value)


class Circle(object):
    # pi = 3.14
    pi = ReadonlyNumber(3.14)

    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return self.pi * self.radius ** 2


print("---1--")
a = Circle(4)
print("---2--")
print(a.area)
print("---3--")
print(a.area)
print("---4--")
