#!/usr/bin/python3

'''
这是注释的内容
#这是内部的注释
'''

import sys
print(sys.version)

list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end = "*")
