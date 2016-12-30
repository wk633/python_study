class IntTuple(tuple):
    def __new__(cls, iterable):
        # cls is class object
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)
    def __init__(self, iterable):
        # before
        # print self
        super(IntTuple, self).__init__(iterable)
        # after

t = IntTuple([1, -1, 'abc', 6, ['x','y'], 3])
print t
print type(t)
