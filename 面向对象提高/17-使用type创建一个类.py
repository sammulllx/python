# 普通定义类的方式
class A:
    pass


# print(help(A))

# 使用type这种特殊方式
bb = type("B", (), {})  # bb就是一个变量指向B类,其实直接用B最直观
# B = type("B", (), {})
# print(help(bb))


A()  # 创建一个A类的实例对象
b = bb()  # 创建一个B类的实例对象

print(bb)
print(id(bb))
print(b)
print(id(b))
