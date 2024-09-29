# 如果将闭包用于装饰器,那么闭包中内部函数里面,是将外部函数中的变量,当做函数使用

def log(func):
    def call():
        ret = func()
        if ret and isinstance(ret, str):
            with open("log.txt", "w") as f:
                f.write(ret)

        return ret

    return call


@log
def print_hello():
    return "hello world"


print(print_hello())


# 如果是普通闭包，那么在闭包中内部函数里面，是将外部函数中的变量我， 当做数据来使用


# def who(name):
#     def do(content):
#         print("(%s):%s" % (name, content))

#     return do


# zhangsan = who("张三")
# lisi = who("李四")

# zhangsan("你努力了吗？")
# lisi("为啥努力！")
# zhangsan("你确定不要努力吗？")
# lisi("嗯，确定？")
# zhangsan("那可就不要要怪别人努力了啊")
# lisi("别人与我何关!")
# zhangsan("隔壁那户人家姓xxxx")
# lisi("( ⊙ o ⊙ )啊！")
