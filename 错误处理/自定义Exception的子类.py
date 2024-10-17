class OldBoyError(Exception):  # 自定义错误类型
    def __init__(self, message='默认'):
        self.message = message
        print("实例化")

    def __str__(self):  # 打印异常的时候会调用对象里面的__str__方法返回一个字符串
        return '自定义的子类输出:'+self.message


try:
    # 当你写 raise OldBoyError 时，Python 会隐式地创建一个 OldBoyError 实例。
    raise OldBoyError  # raise是主动抛出异常，可以调用自定义的异常抛出异常
except OldBoyError as e:
    print(e)
