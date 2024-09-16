class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return  'C'
# 1.通过实例调用方法：
# 正确的方式是通过实例对象调用 print_score 方法，这样 self 会自动绑定为实例对象。
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
bart.print_score()
lisa.print_score()
# 通过类调用，但传入实例（不推荐）：
# 你也可以通过类名调用方法，但你必须显式传入实例作为参数。
Student.print_score(bart)
Student.print_score(lisa)

print(bart.name,bart.get_grade())
print(lisa.name,lisa.get_grade())

