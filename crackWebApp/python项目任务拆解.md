python项目任务拆解

#### python访问数据库



#### logging方式调试



#### functools



#### 理解\_\_exit\_\_, \_\_enter\_\_

http://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit

```Python
class controlled_execution:
  def __enter__(self):
    set things up
    return thing
  def __exit__(self, type, value, traceback):
  	tear things down

with controlled_execution() as thing:
	some code
```

with语句执行会调用enter方法，返回值是as的那个变量



#### with语句

http://effbot.org/zone/python-with-statement.htm





#### threadlocal



#### 多线程／多进程





