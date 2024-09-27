# 针对不带参数的decorator：
# import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print('2024-6-1')


# now()
# print(now.__name__)


# 或者针对带参数的decorator：

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2024-6-1')


now()
print(now.__name__)
