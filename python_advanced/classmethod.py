# -*- coding:utf-8 -*-
class Person(object):

    __count = 0

    @classmethod
    # 定义的是类方法
    def how_many(cls):
        return cls.__count
    def inputScore(cls, score):
        cls.score = score

    def __init__(self, name):
        self.name = name
        Person.__count += 1

print Person.how_many()

p1 = Person('Bob')
print Person.how_many()


p1.inputScore(98)
print p1.score

Person.inputScore(99)
print Person.score
