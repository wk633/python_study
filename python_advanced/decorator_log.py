# -*- coding: utf-8 -*-

def log(f):
	def fn(*args, **kw):
        # 确保不管多少个参数都能正常调用
		print 'call ' + f.__name__ + '()...'
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
