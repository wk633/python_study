class Person(object):
    __count = 0
    def __init__(self, name):
        Person.__count += 1
        print Person.__count
        self.name = name

p1 = Person('Bob')
p2 = Person('Alice')

try:
    print Person.__count
except AttributeError:
    print 'attributeerror'
