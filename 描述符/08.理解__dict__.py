class C:
    x = 1
    '''
    说明文档
    '''
    leishuxing = 99

    def __init__(self, y):
        self.y = y

    def fun(self):
        print(self.y)


c = C(2)
print(c.__dict__)

print(C.__dict__)

print(type(c).__dict__)

print(vars(c))

c.fun()

c.__dict__['y']
'''假如 aa 指向一个实例对象。

1. 程序会先查找 aa._dict_['m']是否存在，如果存在则调用。 
2. 如果步骤 1 不存在，则到 type(aa).dict['m']中查找，如果存在则调用。 
3. 如果步骤 2 不存在，则找 type(aa)的父类。 
4.  以此类推，如果在 object 类中依然没有找到，则调用__getattr__方法，这个方法就是用来存储当属性找不到的时候要执行的处理。注意：在步骤 1、2、3 期间找到的是普通属性就直接使用，如果找到的是一个描述符，则调用__get__方法。'''
