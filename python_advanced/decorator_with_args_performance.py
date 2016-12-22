# -*- coding:utf-8 -*-
import functools
import time

def performance(unit):
    def decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if unit == 'ms':
                t = 1000 * (t2 - t1)
            else:
                t = t2 - t1
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
print '潜在的问题： factorial.__name__等属性变了. factorial.__name__: ', factorial.__name__
