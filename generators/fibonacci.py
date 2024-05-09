def generate_fibonacci_upto(r):
    a, b = 0, 1
    while a < r:
        yield a
        a, b = b, b + a