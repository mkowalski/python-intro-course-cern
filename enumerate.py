from itertools import izip, count


def genumerate(iterable, start=0):
    for elem in iterable:
        yield (start, elem)
        start += 1


def ienumerate(iterable, start=0):
    return izip(count(start=start), iterable)


class cenumerate():

    def __init__(self, iterable, start=0):
        self._iterable = iter(iterable)
        self._count = start - 1

    def __iter__(self):
        return self

    __next__ = next

    def next(self):
        self._count += 1
        return self._count, next(self._iterable)
