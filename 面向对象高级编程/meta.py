class MyClass:
    def __new__(cls, *args, **kwargs):
        print("调用 __new__ 方法")
        instance = super().__new__(cls)  # 创建实例
        return instance

    def __init__(self, value):
        print("调用 __init__ 方法")
        self.value = value


obj = MyClass(10)
