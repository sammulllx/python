class Game_zwdzjs():
    """
    植物大战僵尸类
    """

    def __init__(self):
        self.sun_num = 0


# 创建游戏对象
game = Game_zwdzjs()

# 点击一次阳光，数量+50
game.sun_num += 50

# 请问：假如说Game_zwdzjs类是另外一个开发人员设计的，而在对阳光数量加操作时，可能会出现不小心将+50写为了+500，这是不对的，因为每次都是加50才对，那么想想此时，我们应该怎样对sun_num这个属性进行防护呢？
# 通过property属性 实例对象.属性 = xxx的时候,会自动调用某个方法,在这个方法中对数据校验
