#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 可变参数

import sys


def hello(greeting, *args):
    if (len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def calc_pro(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


hello('Hi')  # => greeting='Hi', args=()
hello('Hi', 'Sarah')  # => greeting='Hi', args=('Sarah')
# => greeting='Hello', args=('Michael', 'Bob', 'Adam')
hello('Hello', 'Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names)  # => greeting='Hello', args=('Bart', 'Lisa')

print(sys.version)

print(calc((1, 2, 3)))  # 传入一个 turple 元组
print(calc([1, 2, 3]))  # 传入一个 list 数组

print(calc_pro(1, 2, 3, 4))
print(calc_pro())
nums = [1, 2, 3]
print(calc_pro(nums[0], nums[1], nums[2]))
# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(calc_pro(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
