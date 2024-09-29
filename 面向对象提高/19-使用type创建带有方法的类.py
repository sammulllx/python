
Foo = type('Foo', (), {'bar': True})


def echo_bar(self):  # 定义了一个普通的函数
    print(self.bar)


# 让FooChild类中的echo_bar属性，指向了上面定义的函数
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

print(hasattr(Foo, 'echo_bar'))  # 判断Foo类中 是否有echo_bar这个属性


print(hasattr(FooChild, 'echo_bar'))  # 判断FooChild类中 是否有echo_bar这个属性


my_foo = FooChild()

my_foo.echo_bar()
