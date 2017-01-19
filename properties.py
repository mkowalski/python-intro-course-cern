class Rect(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def a(self):
        return self.w * self.h

    def seta(self, new):
        self.w = float(new) / self.h

    a = property(fget=a, fset=seta)


class Rect(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def a(self):
        return self.w * self.h

    @a.setter
    def a(self, new):
        self.w = float(new) / self.h


r = Rect(2, 3)
assert r.w == 2; assert r.h == 3; assert r.a == 6

r.w = 4
assert r.w == 4; assert r.h == 3; assert r.a == 12

r.a = 6
assert r.w == 2; assert r.h == 3; assert r.a == 6
