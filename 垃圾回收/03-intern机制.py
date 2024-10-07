a1 = "HelloWorld"
a2 = "HelloWorld"
a3 = "HelloWorld"
a4 = "HelloWorld"
a5 = "HelloWorld"
a6 = "HelloWorld"
a7 = "HelloWorld"
a8 = "HelloWorld"
a9 = "HelloWorld"


'''

python会不会创建9个对象呢？在内存中会不会开辟9个”HelloWorld”的内存空间呢？ 
想一下，如果是这样的话，我们写10000个对象，比如a1=”HelloWorld”…..
a1000=”HelloWorld”， 那他岂不是开辟了1000个”HelloWorld”所占的内存空间了呢？
如果真这样，内存不就爆了吗？所以python中有这样一个机制——intern机制，让他只占用
一个”HelloWorld”所占的内存空间。靠引用计数去维护何时释放。
'''

# 单个单词，不可修改，默认开启intern机制，共用对象，引用计数为0，则销毁
a = 'abcde'
b = 'abcde'
c = 'abcde'
print(id(a))
print(id(b))
print(id(c))
# 140650676172528
# 140650676172528
# 140650676172528

# 字符串（含有空格），不可修改，没开启intern机制，不共用对象，引用计数为0，销毁
aa = 'hello    world '
bb = 'hello    world '
print(id(aa))
print(id(bb))

# 140650664167088
# 140650673881264
