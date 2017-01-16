def make_adder(n):
    def adder(x):
        return n + x

    return adder


add3 = make_adder(3)
add9 = make_adder(9)
print add3(4), add9(4)


def make_adder_2(n):
    return lambda x: n + x


add2 = make_adder_2(2)
print add2(4)

make_adder_3 = lambda x: lambda y: x + y
add4 = make_adder_3(4)
print add4(4)
