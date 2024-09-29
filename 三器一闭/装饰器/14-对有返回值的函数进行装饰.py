# def xxx(func):
#     def yyy(*args, **kwargs):  # 用来接收不确定个数的参数
#         ret = func(*args, **kwargs)  # 用来收到参数 进行拆包,然后传递到原函数中
#         return ret
#     return yyy


# @xxx  # 相当于a = xxx(a)
# def a(num):
#     print("-----1", num)
#     return 100, 200, 300


# ret = a(100)
# print(ret)
from time import ctime, sleep


def timefun(func):
    def wrapped_func():
        print("%s called at %s" % (func.__name__, ctime()))
        # 这里应该加上return ，及时func指向的函数没有返回值，那么默认也是None，
        # 此时无非是return None而已，也是可以的
        return func()
    return wrapped_func


@timefun
def foo():
    print("I am foo")


@timefun
def get_info():
    return '----hahah---'


foo()
sleep(2)
foo()

print(get_info())  # 可以看到这里并没有 get_info这个函数 返回的数据，因此这里有不完善的地方
