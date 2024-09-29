class Goods(object):
    @property
    def size(self):
        return 100


obj = Goods()
ret = obj.size
print(ret)
