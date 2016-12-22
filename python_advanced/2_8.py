def calc_prod(lst):
    def lazy_calc():
        def f(x,y):
            return x*y
        return reduce(f, lst)
    return lazy_calc

f = calc_prod([1, 2, 3, 4])
print f()
