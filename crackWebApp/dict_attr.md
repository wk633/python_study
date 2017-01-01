改造dict类实现支持 x.y访问

原理
从对象中读取属性 调用的是 self.\_\_getattr\_\_
设置属性 调用的是 self.\_\_setattr\_\_
