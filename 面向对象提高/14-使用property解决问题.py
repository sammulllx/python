class Game_zwdzjs():
    """
    植物大战僵尸类
    """

    def __init__(self):
        self.__sun_num = 0

    @property
    def sun_num(self):
        print("---4---")
        return self.__sun_num

    @sun_num.setter
    def sun_num(self, num):
        print("---5---")
        if num == 50:
            self.__sun_num += num
            return "ok"
        return "error"


# 创建游戏对象
game = Game_zwdzjs()

print("---0---")
print(game.sun_num)
print("---1---")
# 点击一次阳光，数量+50
game.sun_num += 50  # game.sun_num = game.sun_num + 50
print("---2---")
print(game.sun_num)
print("---3---")
