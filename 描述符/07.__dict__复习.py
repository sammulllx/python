class A:
    '''
    说明文档
    '''
    leishuxing = 99

    def __init__(self):
        self.a = 10
        self.b = 20

    def xxx(self):
        pass


p = A()
print(p.__dict__)  # {'a': 10, 'b': 20}
print(A.__dict__)
