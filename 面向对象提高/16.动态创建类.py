def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


a = choose_class('foo')
a()  # 会执行第3行定义的那个类中的__new__和__init__当然,需要手动写上

b = choose_class('FOO')
b()  # 会执行第7行定义的那个类中的__new__和__init__当然,需要手动写上
