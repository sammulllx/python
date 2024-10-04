

class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if hasattr(cls, '_instance'):
            return getattr(cls, '_instance')
        print(super())
        obj = super().__call__(*args, **kwargs)
        setattr(cls, '_instance', obj)
        return obj


class Person(metaclass=SingletonMeta):
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
