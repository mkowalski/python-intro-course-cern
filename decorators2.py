def return_self(fn):
    def proxy(self, *args, **kwargs):
        fn(self, *args, **kwargs)
        return self
    return proxy


def chain(names):
    def decorator(cls):
        for name in names:
            setattr(cls, name, return_self(getattr(cls, name)))
        return cls
    return decorator


@chain('add sub'.split())
class Foo(object):

    def __init__(self, n):
        self.n = n

    def add(self, n):
        self.n += n

    def sub(self, n):
        self.n -= n


print Foo(10).add(3).sub(20).n
