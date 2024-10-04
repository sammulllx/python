class ObjectCreator(object):
    pass


a = ObjectCreator()  # a是一个实例对象
print(a)
b = a  # b也指向a指向的那个实例对象
A = ObjectCreator  # 让A也指向OjectCreator指向的类对象
c = A()
print(c)
print('---')
print(hasattr(ObjectCreator, 'new_attribute'))
ObjectCreator.new_attribute = 'foo'  # 为类增加属性
print(hasattr(ObjectCreator, 'new_attribute'))

print(hasattr(a, 'new_attribute'))
del A.new_attribute
print(hasattr(a, 'new_attribute'))
