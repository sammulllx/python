def xxx(func):
    def yyy(*args, **kwargs):  # 用来接收不确定个数的参数
        func(*args, **kwargs)  # 用来收到参数 进行拆包,然后传递到原函数中
    return yyy


@xxx  # 相当于a = xxx(a)
def a(num):
    print("-----1", num)


@xxx
def b(num, num2):
    print("-----2", num, num2)


@xxx
def c(num, num2, num3):
    print("-----3", num, num2, num3)


a(1)
b(1, 2)
c(1, 2, 3)
