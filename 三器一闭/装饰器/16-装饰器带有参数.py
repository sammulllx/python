import time


def call_out2(timeout=0):
    def call_out1(func):
        def call():
            print("----1----")
            time.sleep(timeout)
            ret = func()
            print("----2----")
            return ret
        return call
    return call_out1


# 下面的装饰过程
# 1. 调用timefun_arg("itcast") 得到一个返回值，即time_fun
# 3. 然后执行time_fun(foo) 得到一个返回值，即wrapped_func
# 4. 让foo = wrapped_fun，即foo现在指向wrapped_func
@call_out2(2)
def print_hello():
    print("hello world")
    return "ok"


print(print_hello())
