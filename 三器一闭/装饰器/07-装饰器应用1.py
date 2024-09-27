def check_login(func):
    def inner():
        # 验证1
        if "admin" != input("请输入用户名:"):
            return "用户名不正确"
        # 验证2
        if "123456" != input("请输入密码:"):
            return "密码不正确"
        # 验证3
        if "7788" != input("请输入手机短信验证码:"):
            return "验证码不正确"

        func()

    return inner


@check_login
def f1():
    print('f1')


f1()  # 调用f1函数
