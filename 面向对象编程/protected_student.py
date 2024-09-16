class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self._score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self._score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self._score

    def set_score(self, score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)

bart.set_score(100)
print(bart.get_name())
print(bart.get_score())

# 不推荐用这种方式调用函数
print(Student.get_name(bart))
print(Student.get_score(bart))
