class Foo:
    def get_bar(self):
        return 'teacher'

    BAR = property(get_bar)


obj = Foo()
res1 = obj.BAR  # 自动调用get_bar方法，并获取方法的返回值
res2 = Foo.BAR
print(res1)
print(res2)
