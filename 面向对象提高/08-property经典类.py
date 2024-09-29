# coding=utf-8
class Goods:
    @property
    def price(self):
        return 100


obj = Goods()
result = obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
print(result)
