def fib_generator():
    num1 = 1
    num2 = 1
    temp_num = num1
    num1, num2 = num2, num1+num2
    yield temp_num

    temp_num = num1
    num1, num2 = num2, num1+num2
    yield temp_num

    temp_num = num1
    num1, num2 = num2, num1+num2
    yield temp_num

    return "已经生成了3个斐波那契数列的值..."


fib = fib_generator()

print(next(fib))
print(next(fib))
print(next(fib))
# print(next(fib))
try:
    print(next(fib))
except StopIteration as ret:
    print(ret.value)
