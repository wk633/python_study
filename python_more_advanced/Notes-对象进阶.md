### 标准继承框架

```Python
class IntTuple(tuple):
    def __init__(self, iterable):
        # before
        super(IntTuple, self).__init__(iterable)
        # after
```



#### \_\_new\_\_

用于实例化，修改对象的实例化方法需要自己写

##### new和init的区别与联系

1. new在init之前调用
2. new至少要有有一个参数cls，代表要实例化的类，此参数自动提供
3. new必须要有返回值，返回实例化出来的类，可以选择用父类实例化出类
4. init有一个参数self，就是new返回的实例

http://www.cnblogs.com/tuzkee/p/3540293.html



### 可管理的对象属性

形式上是属性访问，但实际是调用方法

两种方案

```Python
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

```



### 对象支持比较

```python
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

```



使用functools.total_ordering类装饰器，简化全部的比较

```python
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
```



### 描述符对实例属性做类型检查

场景：属性必须是str int 或者float，如果赋值错误，应该抛出异常

需要实现 \_\_get\_\_, \_\_set\_\_,\_\_delete\_\_描述符方法，用isinstance做类型检查



