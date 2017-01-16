for i, c in zip("ala-ma-kota", range(0, len("ala-ma-kota"))):
    print(i, c)


def my_enumerate(sequence):
    """
    This is non-lazy enumerate function
    """

    return zip(range(len(sequence)), sequence)


for i, c in my_enumerate("ala-ma-kota"):
    print(i, c)
