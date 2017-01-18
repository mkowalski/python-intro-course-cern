from time import time as Time


def fib(n):
    if n < 2:
        return 1
    return fib(n-1)+fib(n-2)


def time(fn, *args):
    start = Time()
    res = fn(*args)
    stop = Time()
    return (stop - start), res


def time2(fn):
    start = Time()
    res = fn()
    stop = Time()
    return (stop - start), res

# print time(fib, 30)
# print time2(lambda: fib(30))


class memo:

    def __init__(self, fun):
        self.fun = fun
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.fun(*args)
        return self.cache[args]


def memo(fun):
    cache = {}

    def func(*args):
        if args not in cache:
            cache[args] = fun(*args)
        return cache[args]
    return func
