class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items - 1
        return val


p = Pager(4)  # 实参2 表示模拟的当前浏览器传递过来的要查询的页数
print(p.start)  # 就是起始值，即：m
print(p.end)  # 就是结束值，即：n


# 总结:
# 创建一个对象的时候,可以给默认的初始值,为了更方便得到某个属性,我们不应该将这些变量的属性
# 当做普通的来使用 而是通过property装饰器,这样当调用属性的时候,自动调用某个方法,这个方法
# 可以根据创建对象时传入的数据计算出一个值,这就做到了更加灵活
