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
