#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()
import types


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):  # 继承

    def run(self):  # 多态
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Huahua(Dog):
    def run(self):
        print("Huahua is running...")


class MyDog(object):
    def __len__(self):
        return 100


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


def fn():
    pass


print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))
print('type(print) =', type(print))
print('type(Animal) =', type(Animal()))


print('type(\'abc\')==str?', type('abc') == str)


print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type((x for x in range(10))) == types.GeneratorType)

a = Animal()
b = Dog()
c = Huahua()

print(isinstance(c, Animal))  # true
print(isinstance(c, Dog))  # true
print(isinstance(c, Huahua))  # true

print(isinstance('a', str))  # true
print(isinstance(123, int))  # true
print(isinstance(b'a', bytes))  # true

# 判断一个变量是否为元组或列表
print(isinstance([1, 2, 3], (list, tuple)))  # true
print(isinstance((1, 2, 3), (list, tuple)))  # true
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法
print(dir('ABC'))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，
# 所以，下面的代码是等价的
print(len('ABC'))
print('ABC'.__len__())

dog = MyDog()
print(len(dog))  # 或直接 print(len(MyDog()))

print('ABC'.lower())

obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x)  # 获取属性'x'
print(hasattr(obj, 'y'))  # 获取属性'y'吗?
setattr(obj, 'y', 19)  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗
print(getattr(obj, 'y'))  # 获取属性'y'
print(obj.y)  # 获取属性'y'

print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404)
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print(fn)  # fn 指向obj.power
print(fn())  # 调用fn()与调用obj.power()是一样的
