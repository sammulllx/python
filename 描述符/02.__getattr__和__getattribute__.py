import time


class A:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):  # 属性存在不存在都调用,优先级高
        # 如果访问的是 'name' 属性，直接返回其值
        # print(item, object.__getattribute__(self, item))
        # print(item, super().__getattribute__(item))
        print('上面')
        return 1000

    # def __getattr__(self, item):  # 属性不存在时调用,如果不写在父类object内也会有,报'A' object has no attribute 'age'
    #     '''
    #     当实例对象访问一个不存在的属性时,此方法会被自动调用,可以在此处进行进一步处理,例如可以产生一个异常等
    #     '''
    #     print('哈哈哈,item = ', item)
    #     raise Exception('不好了,属性不存在')


a = A("小名")
print(a.name)
try:
    print(a.age)
except Exception as e:
    print(e)
