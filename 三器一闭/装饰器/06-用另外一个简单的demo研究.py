def A(func):
    def B():
        print("-----1-----")
        func()
        print("-----2-----")
    return B


@A
def helloworld():
    print("my name is hellowolrd")


helloworld()
