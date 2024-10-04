class Foo:
    @property
    def attr(self):
        print('获取属性attr的值')
        return 'attr的值'

    def bar(self): pass


foo = Foo()
print(foo.attr)

print(type(Foo.attr))
print(type(Foo.bar))
