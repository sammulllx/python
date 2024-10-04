list = [1, 2, 3, 4]
num = 100
print(id(num))


def singleton(cls):
    print(cls.__class__)
    print("step 1")
    list.append(544)
    # global num
    # num = 200
    print(num)

    def inner(*args, **kwargs):
        # print("step 2")
        # obj = cls(*args, **kwargs)
        # return obj
        if hasattr(cls, '__instance'):
            return getattr(cls, '__instance')
        obj = cls(*args, **kwargs)
        setattr(cls, '__instance', obj)
        return obj
    return inner


@singleton
class Person:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    pass


p_1 = Person('sammul', 99)
print(p_1.name)
p_2 = Person('bao', 32)
print(p_2.name)
print(p_1.name)

print(p_1 is p_2)
print(list)


print(num)
