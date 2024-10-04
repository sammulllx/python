def singleton(cls):
    dict = {}  # 利用闭包外部局部变量保存

    def inner(*args, **kwargs):
        if '_instance' in dict:
            return dict['_instance']
        obj = cls(*args, **kwargs)
        dict['_instance'] = obj
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
