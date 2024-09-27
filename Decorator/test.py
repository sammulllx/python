class MyClass:
    class_var = 'I am a class variable'  # 类变量

    def __init__(self, value):
        self.instance_var = value  # 实例变量

# 创建两个实例
obj1 = MyClass('value1')
obj2 = MyClass('value2')

# 访问实例变量
print(obj1.instance_var)  # 输出：value1
print(obj2.instance_var)  # 输出：value2

# 访问类变量
print(MyClass.class_var)  # 输出：I am a class variable
print(obj1.class_var)  # 输出：I am a class variable
print(obj2.class_var)  # 输出：I am a class variable

print('-----------------------')


def func(*args,**kwargs):
    print(args[3])
    print(kwargs['b'])

func(1,2,3,4,5,a=100,b=200)


