class Fib(object):

    def __init__(self, num):
        self.result = []
        for i in xrange(1, num+1):
            self.result.append(self.genFib(i))


    def __len__(self):
        return len(self.result)

    def __str__(self):
        return str(self.result)

    def genFib(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.genFib(n-1)+self.genFib(n-2)

f = Fib(10)
print f
print len(f)
