class Player:
    __instance = None
    __flag = False

    def __new__(cls, *args, **kwargs):
        print("new执行了")
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not Player.__flag:
            print("init执行了")
            Player.__flag = True


video1 = Player()
print(video1)
video2 = Player()
print(video2)