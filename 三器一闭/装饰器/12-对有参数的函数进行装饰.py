from time import ctime, sleep


def timefun(func):
    def wrapped_func(a, b):
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrapped_func


@timefun
def foo(a, b):
    print(a+b)


foo(3, 5)
sleep(2)
foo(2, 4)
# 1.如果被装饰的函数有2个参数，那么在定义闭包的时候，就需要在内部函数中要有2个形参变量

# 2.当调用原函数的时候，实参会传递到闭包中的内部函数的形参变量中，在内部函数执行的时候将这些数据当做实参传递到原函数中
