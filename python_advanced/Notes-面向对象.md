### Notes-面向对象

1. init

   ```python
   class Person(object):
       def __init__(self, name, gender, birth):
           self.name = name
           self.gender = gender
           self.birth = birth
           
   xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
   xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')
   ```

2. 进阶init例子

   ```Python
   class Person(object):
       def __init__(self, name, gender, birth, **kw):
           self.name = name
           self.gender = gender
           self.birth = birth
           for k,v in kw.iteritems():
               setattr(self, k, v)
           

   xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

   print xiaoming.name
   print xiaoming.job
   ```





### 访问限制

如果一个属性以**双下划线**开头，该属性无法被外部访问



### 实例属性和类属性

实例属性每个实例各自拥有，互相独立，而类属性只有一份

类属性每个实例都能访问



### 实例方法和类方法

实例的方法就是在类中定义的函数，

调用实例方法必须在实例上调用

在实例方法内部，可以访问所有实例属性



class中定义的全部是实例方法

如果要定义类方法，需要

```Python
class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        // how_many方法绑定到Person类上
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
```

类方法是在类上调用，因此无法访问获得任何实例变量，只能获得类的引用



###  python的继承

1. 总是从某个类继承

   ```Python
   class MyClass(object):
   	pass
   ```

2. 不忘调用`super().__init__`

   ```python
   def __init__(self, args):
   	super(SubClass, self).__init__(args)
       pass
   ```

3. 例子

   self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）

   ```python
   class Person(object):
       def __init__(self, name, gender):
           self.name = name
           self.gender = gender

   class Teacher(Person):
       def __init__(self, name, gender, course):
           super(Teacher, self).__init__(name, gender)
           self.course = course

   t = Teacher('Alice', 'Female', 'English')
   print t.name
   print t.course
   ```

   ​

### python判断是否类型的实例

1. isinstance

   `isinstance(t, Student)`



### python的多重继承

```Python
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
```



### 获取对象信息

1. type() : 获取变量类型
2. dir() : 获取变量的所有属性 





### setattr()与getattr()

setattr(object,name,value):

作用：设置object的名称为name（type：string）的属性的属性值为value，属性name可以是已存在属性也可以是新属性。

getattr(object,name,default):

作用：返回object的名称为name的属性的属性值，如果属性name存在，则直接返回其属性值；如果属性name不存在，则触发AttribetError异常或当可选参数default定义时返回default值。

https://my.oschina.net/DreamG/blog/138551