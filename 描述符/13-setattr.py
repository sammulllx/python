class A:
    pass


a = A()
print(A.__dict__)
print(a.__dict__)
setattr(a, "num", 10)
print(a.__dict__)
print(getattr(a, 'num'))
