import time  # 导入time模块，用于程序中的延时功能


# 定义外部装饰器函数 call_out2
# 这个装饰器的作用是接受一个 timeout 参数，并返回一个装饰器函数 call_out1
def call_out2(timeout=0):
    # 定义内部装饰器函数 call_out1
    # 这个函数接受另一个函数（func）作为参数，用于装饰实际的功能函数
    def call_out1(func):
        # 定义最内部的函数 call，实际用于对被装饰函数的执行进行包装
        def call():
            # 第一步，打印提示信息，表示函数即将执行
            print("----1----")
            # 第二步，暂停执行 timeout 秒（通过外部函数 call_out2 传入的参数控制）
            time.sleep(timeout)
            # 第三步，执行被装饰的函数（func），并将其返回值赋给变量 ret
            ret = func()
            # 第四步，打印提示信息，表示函数已经执行完毕
            print("----2----")
            # 第五步，返回被装饰函数的返回值
            return ret
        # 返回最内部的函数 call，这个函数就是实际被执行的内容
        return call
    # 返回装饰器函数 call_out1
    return call_out1


# 使用装饰器语法糖 @call_out2(2) 来装饰 print_hello 函数
# 实际上，call_out2(2) 会首先执行，返回 call_out1 装饰器
# 然后 @call_out1(print_hello) 会执行，使得 print_hello 函数被 call 函数包装
@call_out2(2)
def print_hello():
    # 定义要打印的内容
    print("hello world")
    # 返回 "ok" 字符串作为函数的返回值
    return "ok"


# 调用 print_hello 函数，注意这里 print_hello 已经被 call 函数包装
# 因此实际执行的是 call 函数，而不是直接执行 print_hello 函数
# 调用过程将会有2秒的延时，且会有打印提示信息
print(print_hello())  # 打印被包装函数的返回值 "ok"
