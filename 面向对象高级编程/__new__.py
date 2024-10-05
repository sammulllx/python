class MyClass:
    def __new__(cls, *args, **kwargs):
        print("调用 __new__ 方法")
        print('args:', args)
        print('kwargs:', kwargs)
        instance = super().__new__(cls)  # 创建实例
        return instance

    def __init__(self, value, *args, **kwargs):
        print("调用 __init__ 方法")
        self.value = value

    def __repr__(self) -> str:
        return "hello, is __repr__"


obj = MyClass(10, 20, a=1, b=2)
print(obj.value)
obj
