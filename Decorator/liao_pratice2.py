'''
在装饰器中，常常需要判断第一个参数是否是一个函数，以便决定装饰器的行为。
如果你直接使用装饰器（如 @log），第一个参数就是目标函数；如果使用带参数的装饰器
（如 @log('execute')），则第一个参数是字符串。
'''
import functools


def log(*args):
    # 检查是否直接传入了函数
    if len(args) == 1 and callable(args[0]):
        func = args[0]
        return create_wrapper(func)

    # 如果传入了参数，返回装饰器
    text = args[0]

    def decorator(func):
        return create_wrapper(func, text)

    return decorator


def create_wrapper(func, text=None):
    @functools.wraps(func)
    def wrapper(*args1, **kwargs):
        print('begin call')
        if text:
            print(f'now execute: {func.__name__}, args: {text}')
        else:
            print(f'now execute: {func.__name__}')
        result = func(*args1, **kwargs)
        print('end call')
        return result

    return wrapper

# 示例用法


@log
def f1():
    print("Function f1")


@log('execute')
def f2():
    print("Function f2")


# 调用函数
f1()
f2()  # 如果需要调用 f2，可以取消注释
