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

   ​



### setattr()与getattr()

setattr(object,name,value):

作用：设置object的名称为name（type：string）的属性的属性值为value，属性name可以是已存在属性也可以是新属性。

getattr(object,name,default):

作用：返回object的名称为name的属性的属性值，如果属性name存在，则直接返回其属性值；如果属性name不存在，则触发AttribetError异常或当可选参数default定义时返回default值。

https://my.oschina.net/DreamG/blog/138551