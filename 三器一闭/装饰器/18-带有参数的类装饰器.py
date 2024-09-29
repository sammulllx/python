class Test(object):
    def __init__(self, num):
        print("---初始化---")
        self.__num = num

    def __call__(self, func):
        print("---call---")
        self.__func = func
        return self.call_old_func

    def call_old_func(self):
        print('---开始调用装饰器的功能1---')
        self.__func()
        print('self.__num的值为%d' % self.__num)
        print('---开始调用装饰器对功能2---')


@Test(101)
def test():
    print("----test---")


test()  # 如果把这句话注释，重新运行程序，依然会看到"--初始化--"
