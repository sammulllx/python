from time import ctime, sleep

# 定义一个闭包


def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        func()
    return wrapped_func


@timefun  # 使用装饰器对foo进行装饰，此时相当于foo = timefun(foo)
def foo():
    print("I am foo")


foo()  # 相当于调用的是wrapped_func函数
sleep(2)
foo()  # 相当于调用的是wrapped_func函数
