class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def __lt__(self, obj):
        return self.area() < obj.area()

r1 = Rectangle(3,4)
r2 = Rectangle(5,6)
print r1 < r2

print 'using total_ordering'
from functools import total_ordering
@total_ordering
class Rectangle_2(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def __gt__(self, obj):
        return self.area() > obj.area()
    def __eq__(self, obj):
        return self.area() == self.area()

r1 = Rectangle_2(3,4)
r2 = Rectangle_2(5,6)
print r1 < r2
print r1 == r2
print r1 > r2
print r1 <= r2
print r1 >= r2
