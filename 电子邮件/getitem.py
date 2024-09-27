class MyClass:
    def __init__(self):
        # 初始化一个字典作为示例
        self.my_dict = {'a': 1, 'b': 2, 'c': 3}

    def __getitem__(self, key):
        return self.my_dict[key]


# 创建类的实例
obj = MyClass()

# 使用 `[]` 访问字典中的元素
print(obj['a'])  # 输出: 1
print(obj['b'])  # 输出: 2

print(obj)

print(obj.my_dict)
