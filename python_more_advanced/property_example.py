from math import pi

class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError('wrong type: ')

        self.__radius = float(value)
    R = property(getRadius, setRadius)

c = Circle(3.2)
print c.R
c.R = 5.2
print c.R
try:
    print c.__radius
except AttributeError, e:
    print e
    # raise AttributeError('not exist')


class Circle_2(object):
    def __init__(self, radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float, long)):
            raise ValueError('wrong type')
        self.__radius = value

c = Circle_2(4.2)
print c.radius
c.radius= 6.2
print c.radius
