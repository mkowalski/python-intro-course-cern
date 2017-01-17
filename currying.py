from functools import partial


def addem(a, b, c, d):
    return a + b + c + d


add4 = partial(addem, 4)

print addem(1, 2, 3, 4)
print add4(1, 2, 3)
print partial(addem, 4)(1, 2, 3)
print partial(addem, c=4)(1, 2, d=3)
