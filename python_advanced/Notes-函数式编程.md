### 高阶函数

1. 变量可以指向函数

   ```python
   f = abs
   f(-20)
   ```

2. 能够接收函数作为参数的函数就是 **高阶函数**

3. **map**

   ```Python
   def format_name(s):
       return s[0].upper() + s[1:].lower()

   print map(format_name, ['adam', 'LISA', 'barT'])
   ```

   map不改变原有序列，返回一个新序列

4. **reduce**

   ```python
   def f(x, y):
       return x + y
   # 第三个值为初始值
   reduce(f, [1, 3, 5, 7, 9], 100)
   ```

5. **filter**

   ```python
   def is_odd(x):
       return x % 2 == 1
   filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
   ```

   filter不改变原有序列，返回一个新序列

   ```python
   import math

   def is_sqr(x):
       r = int(math.sqrt(x))
       return r*r == x

   print filter(is_sqr, range(1, 101))
   ```

6. **sorted**

   ```python
   def cmp_ignore_case(s1, s2):
       if s1[0].lower() < s2[0].lower():
           return -1
       elif s1[0].lower() > s2[0].lower():
           return 1
       else:
           return 0

   print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

   # 规则
   # 比较函数的定义是，传入两个待比较的元素 x, y，
   # 如果 x 应该排在 y 的前面，返回 -1，
   # 如果 x 应该排在 y 的后面，返回 1。
   # 如果 x 和 y 相等，返回 0
   ```

7. 返回函数 (涉及到闭包的问题)

   ```Python
   def calc_prod(lst):
       def lazy_calc():
           def f(x,y):
               return x*y
           return reduce(f, lst)
       return lazy_calc

   f = calc_prod([1, 2, 3, 4])
   print f()
   ```

8. 闭包（closure）

   内层函数引用了外层函数的变量，然后外层函数返回内层函数的情况，叫做闭包

   **闭包**的特点：返回的函数还引用外层函数的局部变量

   使用闭包的时候要确保引用的局部变量在函数返回后不能变

   ```Python
   # -*- coding: utf-8 -*-

   def count():
       fs = []
       for i in range(1, 4):
           def f():
               return i*i
           fs.append(f)
       return fs

   f1, f2, f3 = count()
   print f1(), f2(), f3()

   def count_new():
       fs = []
       for i in range(1,4):
           def f(j):
               def g():
                   return j*j
               return g
           r = f(i)
           fs.append(r)
       return fs

   f1, f2, f3 = count_new()

   print f1(), f2(), f3()
   ```

9. 匿名函数

   ```Python
   map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
   >> [1, 4, 9, 16, 25, 36, 49, 64, 81]

   sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))
   >> [9, 5, 3, 1, 0]

   print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
   ```

   匿名函数限制只能有一个表达式，不写return，返回值就是该表达式的结果

   ​

10. **装饰器**

   定义了一个函数，想在运行时动态的增加功能，又不想改动函数本身的代码

   于是想到高阶函数，可以编写一个高阶函数，接收一个函数对其包装，然后返回一个新函数

```python
 def f1(x):
   	return x*2

   # new_fn即用高阶函数实现了装饰器的目的
def new_fn(f):
   	def fn(x):
   		print 'xxxxx'
   		return f(x)
   	return fn

f1 = new_fn(f1)
print f1(5)
```

   

   Python内置的@语法就是为了简化装饰器的调用

```python
@new_fn
def f1(x):
   	return x*2


# 以上代码的功效于
def f1(x):
    return x*2
f1 = new_fn(f1
```

​	

​	优点：简化代码，避免重复代码

​			比如可以 打印日志 @log

​			检测性能 @performance

​			数据库事务 @transaction

​			url路由：@post('/register')

​	

### 无参数装饰器

```Python
def log(f):
	def fn(*args, **kw):
        # 确保不管多少个参数都能正常调用
		print 'call' + f.__name__ + '()...'
		return f(*args, **kw)
	return fn

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

@log
def add(x, y):
    return x + y
print add(1, 2)
```



```Python
import time

def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2-t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)
```



### 带参数装饰器

需求：装饰器能根据参数判断增加的功能

```python
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
```



### 解决decorator潜在的问题

由于经过装饰器后原函数的信息（比如函数名）被新函数覆盖，因此需要继承一下

```Python
import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
```



### 偏函数

functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了

```Python
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85




import functools

sorted_ignore_case = functools.partial(sorted, cmp = lambda s1, s2: cmp(s1.upper(), s2.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])
```







### 理解 *arg、 **kw

*arg： 关键字参数，用于元组

**kw：关键字参数，用于字典

```python
def tupleArgs(arg1, arg2= 'B', *arg3):
    print('arg 1:%s ' % arg1)
    print('arg 2:%s ' % arg2)
    for eachArgNum in range(len(arg3)):
        print('the %d in arg 3 :%s ' % (eachArgNum,arg3[eachArgNum]))
if __name__ == '__main__':
    tupleArgs('A')
    #   arg 1:A
    #   arg 2:B
    tupleArgs('23','C')
    #   arg 1:23
    #   arg 2:C
    tupleArgs('12','A','GF','L')
    #   arg 1:12
    #   arg 2:A
    #   the 0 in arg 3 :GF
    #   the 1 in arg 3 :L 
```



参考： http://www.imooc.com/qadetail/79469



### functools模块

1. partial
2. update_wrapper
3. wraps
4. reduce
5. cmp_to_key
6. Total_ordering

http://www.wklken.me/posts/2013/08/18/python-extra-functools.html