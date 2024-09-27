try:
    print(next(fib))
except StopIteration as ret:
    print(ret.value)