class MyClass:
    def __init__(self):
        # 初始化一个空字典
        self.my_dict = {}

    def __setitem__(self, key, value):
        self.my_dict[key] = value

    def __getitem__(self, key):
        return self.my_dict[key]


# 创建类的实例
obj = MyClass()

# 使用 `[]` 语法设置键值对
obj['a'] = 10
obj['b'] = 20

# 使用 `[]` 访问已设置的值
print(obj['a'])  # 输出: 10
print(obj['b'])  # 输出: 20
