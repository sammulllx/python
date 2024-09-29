class Foo(object):
    bar = True  # 类属性


Foo2 = type("Foo2", (object,), {'bar': True})

a = Foo()
b = Foo2()

print(a.bar)
print(b.bar)
