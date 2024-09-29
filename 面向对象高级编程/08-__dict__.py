class A(object):
    def __init__(self):
        self.a = 100
        self.b = 200
        self.c = "hello"


a = A()
print(a.__dict__)  # {'a': 100, 'b': 200, 'c': 'hello'}
# 说明:
# 如果一个对象使用了__dict__打印结果,那么会看到一个字典,这个字典中key-value表示的是这个对象中的属性和属性指向的数据
# 属性当做key,数据当做value
