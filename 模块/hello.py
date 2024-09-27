#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '  # 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'Michael Liao'

import sys


def test():
    args = sys.argv
    print('Arguments:', args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == '__main__':
    test()
# 将__main__改为 hello就会发现在python交互环境里import hello.py也会直接打印出'Hello,world!'了，
# 也就验证了在导入模块时__name__是模块名
