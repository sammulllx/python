class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):  # 继承

    def run(self):  # 多态 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Timer(object):
    def run(self):
        print('Start...')


def run_twice(a):
    a.run()
    a.run()


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()


a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型


print(isinstance(a, list))  # true
print(isinstance(b, Animal))  # true
print(isinstance(c, Dog))  # true
print(isinstance(c, Animal))  # true
# 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。
# 但是，反过来就不行
print(isinstance(b, Dog))  # false


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())
run_twice(Timer())
