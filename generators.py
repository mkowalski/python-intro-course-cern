def generate_fib():
    f1, f2 = 1, 0
    while True:
        yield f1
        f1, f2 = f1 + f2, f1
