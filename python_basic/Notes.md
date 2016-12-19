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

   ​

