def one(*args):
    return args


def two(b=1, c=2):
    return b, c


def three(*args, **kwds):
    """
    *args collects all remaining positional arguments
    **kwds collects all remaining keyword arguments
    """
    return args, kwds


def four(a, b=1, *args, **kwds):
    return a, b, args, kwds


print one(1, 2, 3)
print two(4, 5)
print three(1, 2, 3, a='a', b='b')
print four(1, 2, 3, d='d')
