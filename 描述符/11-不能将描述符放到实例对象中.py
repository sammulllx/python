class NameDes(object):
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        print('_get_被调用')
        return self._name

    def __set__(self, instance, value):
        print('set_被调用')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('必须是字符串')


class Person(object):
    # name = NameDes()  # 类属性时 描述符才有作用

    def __init__(self):
        self.name = NameDes()  # 实例属性时 不会起到描述符的作用


p = Person()
print(p.name)

'''
如果将描述符对象复制给实例属性,此时相当于name指向了一个个普通的对象,只不过这个对象中有__get__、
__set__方法罢了,不会自动调用期期__get__方法
而如果是类属性是一个描述符则会自动调用__get__方法
'''
