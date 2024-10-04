class A:
    def xxx(self):
        pass


def func():
    pass


a = A()
print(a.xxx)
print(a.xxx.__name__)
print(func)
print(func.__name__)
