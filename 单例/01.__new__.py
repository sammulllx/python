class Player:
    __instance = None
    __flag = False

    def __new__(cls, *args, **kwargs):  # 静态方法
        print("new执行了")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print('新建的实例地址为%d' % id(cls.__instance))
        return cls.__instance

    def __init__(self):
        if not Player.__flag:
            print("init执行了")
            Player.__flag = True


video1 = Player()
print(video1)
print(id(video1))
video2 = Player()
print(video2)
# class A(object):
#     def __init__(self, *args, **kwargs):
#         print("init &&&&  %s" % self.__class__)

#     def __new__(cls, *args, **kwargs):
#         print("new &&&&  %s" % cls)
#         return super().__new__(cls, *args, **kwargs)

# a = A()
