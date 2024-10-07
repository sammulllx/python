import sys
import gc
a = "hello wrold"
print(sys.getrefcount(a))
# 可以查看a对象的引用计数,但是比正常计数大1,因为调用月函数的时候传入a,这会让a的引用计数+1
print(gc.get_threshold())
'''
清理第 0 代的链子的条件是垃圾数据达到 700 个；
当第 0 代链子清理的次数达到 10 次时,第 1 代链子进行一次清理；
当第 1 代链子清理的次数达到 10 次时，第 2 代链子进行一次清理。
'''


print(gc.get_count())
