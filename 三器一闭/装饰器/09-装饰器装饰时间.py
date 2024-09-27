def timefun(func):
    print("----开始装饰----")

    def wrapped_func():
        print("----开始调用原函数----")
        func()
        print("----结束调用原函数----")

    print("----完成装饰----")
    return wrapped_func


@timefun
def helloworld():
    print("helloworld")


helloworld()  # 注意此时并没有调用函数helloworld，如果运行结果中出现了一些信息，则说明@timefun开始装饰
# 的时间是Python解释器在遇到那句代码时进行，而不是因为调用被装饰的函数才开始装饰
