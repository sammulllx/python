class PointXY(object):
    """
    通过迭代器，生成不确定个数的点的坐标
    """

    def __init__(self):
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        temp_y = 2 * self.x + 1
        temp_point_x_y = (self.x, temp_y)  # 得到一个元组
        self.x = temp_y
        return temp_point_x_y


point_x_y = PointXY()  # 创建一个可迭代对象
point_x_y_iter = iter(point_x_y)  # 获取迭代器

point_x_y_1 = next(point_x_y_iter)
print(point_x_y_1)

point_x_y_2 = next(point_x_y_iter)
print(point_x_y_2)

point_x_y_3 = next(point_x_y_iter)
print(point_x_y_3)

point_x_y_4 = next(point_x_y_iter)
print(point_x_y_4)
