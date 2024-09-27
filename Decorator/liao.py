
def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log
def now():
    print('2018-06-01')


now()
print(now.__name__)
