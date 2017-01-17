from operator import add


def isfloat(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


with open("summing.in") as my_file:
    for line in my_file:
        print reduce(add,
                     map(float,
                         filter(isfloat, line.split())),
                     0)
