class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k,v in zip(names, values):
            self[k] = v
    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

d1 = Dict()
d1['x'] = 100
print d1.x

d1.y = 200
print d1['y']

d2 = Dict(('a','b','c'),(1,2,3))
print d2.a, d2.b, d2.c
