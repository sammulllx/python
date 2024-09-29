# 没有指定metaclass,就是用默认type创建
# class Foo(object):
#     bar = 'bip'
# print(Foo.bar)


def upper_attr(class_name, class_parents, class_attr):
    # class_name 会保存类的名字 Foo
    # class_parents 会保存类的父类 object
    # class_attr 会以字典的方式保存所有的类属性

    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'

# class Foo(object):    #python2用法
#     __metaclass__ = upper_attr  # 设置Foo类的元类为upper_attr
#     bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)
