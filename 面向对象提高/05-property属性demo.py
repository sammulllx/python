# ############### 定义 ###############
'''
	•	Python 3 中：
	•	class Foo:
	•	class Foo():
	•	class Foo(object):

这三种写法在 Python 3 中是等价的，都会定义一个继承自 object 的新式类。

	•	Python 2 中：
	•	class Foo: 定义的是经典类，不继承自 object，与新式类有一些特性差异。
    •   class Foo(): 定义的是经典类，不继承自 object，与新式类有一些特性差异。
	•	class Foo(object): 定义的是新式类，继承自 object，具有更多特性和更一致的行为。

'''


class Foo:
    def func(self):
        print("func被调用")

    # 定义property属性
    @property
    def prop(self):
        print("prop被调用")


# ############### 调用 ###############
foo_obj = Foo()
foo_obj.func()  # 调用实例方法
foo_obj.prop  # 调用property属性，实际上会调用第8行的方法
