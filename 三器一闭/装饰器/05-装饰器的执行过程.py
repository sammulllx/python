def check_login(func):
    def inner():
        # 验证1
        # 验证2
        # 验证3
        func()
    return inner


'''
第一步:
当python解释器遇到下面的@check_login代码时,他会将check_login当做可执行的对象
来调用,即check_login(),并且将下面的f1函数当做实参进行传递,此时变成了check_login(f1)

第二步
将check_login(f1)执行的返回值,当做新的f1的值,即此时f1= check_login(f1),也就是说
f1的指向变成了check_login的返回值
'''


@check_login
def f1():
    print('f1')
