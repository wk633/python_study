## 特殊方法

1. `__str__`

   用于  `print`

   ```Python
   class Person(object):

       def __init__(self, name, gender):
           self.name = name
           self.gender = gender

   class Student(Person):

       def __init__(self, name, gender, score):
           super(Student, self).__init__(name, gender)
           self.score = score

       def __str__(self):
           return "(Student: %s, %s, %s)" % (self.name, self.gender, self.score)
           

   s = Student('Bob', 'male', 88)
   print s
   ```

   ​

2. `__len__`

   用于  `len()`

   ​

3. `__cmp__`

   用于  `cmp`

   ```Python
   class Student(object):

       def __init__(self, name, score):
           self.name = name
           self.score = score

       def __str__(self):
           return '(%s: %s)' % (self.name, self.score)

       __repr__ = __str__

       def __cmp__(self, s):
           if self.score > s.score:
               return -1
           elif self.score < s.score:
               return 1
           else:
               return cmp(self.name, s.name)

   L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
   print sorted(L)

   ```

   ​

### 正确实现特殊方法

1. 只需要编写用到的特殊方法

2. 有关联性的特殊方法都能实现

   \_\_getattr\_\_, \_\_setattr\_\_, \_\_delattr\_\_



### @property 高度封装

需求： 将getter，setter封装成属性调用的样子

原始实现

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
```



引入@property

```Python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
```

`@score.setter`中score是@property下面的方法的名字

```Python
>>> s = Student('Bob', 59)
>>> s.score = 60
>>> print s.score
60
>>> s.score = 1000
Traceback (most recent call last):
  ...
ValueError: invalid score
```



### \_\_slot\_\_

如果需要限制属性的添加，可以用这个

用于指定一个类允许的属性

```Python
class Student(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score
        
>>> s = Student('Bob', 'male', 59)
>>> s.name = 'Tim' # OK
>>> s.score = 99 # OK
>>> s.grade = 'A'
Traceback (most recent call last):
  ...
AttributeError: 'Student' object has no attribute 'grade'
```



### 类实例变可调用对象

```
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend
        
        
>>> p = Person('Bob', 'male')
>>> p('Tim')
My name is Bob...
My friend is Tim...
```



