import math  # import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
from abstest import my_abs
print(my_abs(-100))
# my_abs(1, 2)
# my_abs('A')


def move(x, y, step, angle=0):  # 游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
# 按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


def quadratic(a, b, c):  # 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的两个解。
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if (b*b - 4*a*c) < 0:
        raise TypeError('方程无解')
    x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
    return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
