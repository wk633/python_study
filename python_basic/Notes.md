### Set

1. 判断一个元素是否在set中很快

2. set存储的必须是不变对象

3. 使用例子

   ```python
   weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
   x = '???' # 用户输入的字符串
   if x in weekdays:
       print 'input ok'
   else:
       print 'input error'
   ```

4. 更新

   ```python
   s = set([1,2,3])
   s.add(4)
   s.remove(4) # 如果元素本来不存在，用remove会报错
   ```



### function

1. 递归函数

   ```python
   def fact(n):
       if n==1:
           return 1
       return n * fact(n-1)
   ```

2. 汉诺塔问题较好的参考

   [过程理解的比较好](http://www.jianshu.com/p/3b8a9a2bd9d5)

   [代码精简](http://www.jianshu.com/p/85d6f672eb73)

   ```Python
   #-*- coding:utf-8 -*-

   def hanoi(n, a, b, c):
       # a,b,c 分别表示起始盘，缓存盘和目标盘
       if n == 1:
           print a,'-->', c
           return
       hanoi(n-1, a, c, b) # 将起始柱子上的n-1个盘子移动到缓存盘里
       hanoi(1, a, b, c) # 将起始柱子上最后一个盘子移动到目标盘里
       hanoi(n-1, b, a, c) # 将缓存盘里的n-1个盘子移动到目标盘里

   hanoi(3,'A','B','C')
   ```

3. 可变参数

   ```python
   def average(*args):
       if len(args)!=0:
           return sum(args)*1.0/len(args)
       else:
           return 0.0

   print average()
   print average(1, 2)
   print average(1, 2, 2, 3, 4)
   ```



### 迭代

1. 迭代dict对象

   ```python
   # 值迭代
   d.values()

   # iter值迭代
   d.itervalues()
   ```

   ​

2. 迭代key-value对

   ```python
   d.items()
   d.iteritems()
   ```



3. 生成列表

   ```python
   [x * x for x in range(1, 100, 2)]
   ```

4. 条件过滤

   ```Python
   [x * x for x in range(1, 11) if x % 2 == 0]

   print [100*n1+10*n2+n3 for n1 in range(1,10) for n2 in range(0,10) for n3 in range(0,10) if n1==n3]
   ```









### 零散知识点

1. isinstance(x, str) 可以判断变量 x 是否是字符串
2. 字符串的`upper()`方法可以用于转换成大写