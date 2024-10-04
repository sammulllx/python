class MyDescriptor:
    def __get__(self, instance, owner):
        print('get called')
        return 'get'

    def __set__(self, instance, value):
        print('set called')

    def __delete__(self, instance):
        print('delete called')


class Foo:
    attr = MyDescriptor()


foo = Foo()

print(foo.attr)
print("-"*30)
print(Foo.attr)
print("-"*30)
print(type(foo).attr)
print("-"*30)
print(foo.__class__.attr)
print("-"*30)
print(type(foo).__dict__['attr'].__get__(foo, Foo))
print("*"*30)
foo.attr = 'python'
del foo.attr
