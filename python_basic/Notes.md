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

   http://www.jianshu.com/p/85d6f672eb73