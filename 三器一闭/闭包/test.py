class Person(object):
    def __init__(self, name):
        self.user_name = name

    def say(self, content):

        print("(%s):%s" % (self.user_name, content))


p1 = Person("张三")
p2 = Person("李四")

p1.say("你努力了吗？")
p2.say("为啥努力！")
p1.say("你确定不要努力吗？")
p2.say("嗯，确定？")
p1.say("那可就不要要怪别人努力了啊")
p2.say("别人与我何关!")
p1.say("隔壁那户人家姓xxxx")
p2.say("( ⊙ o ⊙ )啊！")


print('*'*100)
Person.say(p1, "你好")
Person.say(p2, "我很好你好")
