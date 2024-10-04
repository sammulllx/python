import types


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def eat(self):
        print("eat food")


p = Person("小明", "24")
p.habbit = 'football'
Person.sex = None  # 给类Person添加一个属性
setattr(p, 'grade', 99)
print(p.habbit)
print(p.sex)
print(p.grade)

p.eat()


def run(self, speed):
    print("%s在移动, 速度是%dkm/h" % (self.name, speed))


# p.run = run
# p.run(p, 100)  # 虽然这里可以调用aaa指向的函数,但是真正的面向对象开发时,如果调用一个实例方法都不需要传递,而此时传递了,所以不可取

# 下面两行代码的理解:
# 1.调用MethodType,创建一个对象,这个对象中能够明确将来会调用run函数,并将p当作实参传递
# 2.将上一步创建的对象的引用 赋值给p中的run属性
# 3.当执行p.run()的时候,会调用第一步创建的对象,那个对象中会自动调用run函数,并且将p当做实参,此时就模拟完成了给p实例对象添加实例方法
p.run = types.MethodType(run, p)
p.run(180)
