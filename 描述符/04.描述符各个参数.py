class NameDes(object):
    """可以实现描述符的类"""

    def __init__(self):
        self.__name = None

    def __get__(self, instance, owner):  # owner就是Person类
        return self.__name

    def __set__(self, instance, value):
        print("self", self)
        print("instance: ", instance)
        print("value:", value)
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError("必须是字符串")

    def __delete__(self, instance):
        del self.__name


class Person(object):
    # 描述符
    name = NameDes()


p = Person()
p.name = '老师'

print('-----分割线-----')
print(p.name)
