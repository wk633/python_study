### Notes-包与模块

包： 文件夹

模块： xx.py文件



#### 如何区分包和普通目录

包下面必须有 "\_\_init_\_\.py"文件

每层都必须要有



#### 动态导入模块

```Python
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
```



#### \_\_future\_\_

```Python
from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s, unicode)
```



