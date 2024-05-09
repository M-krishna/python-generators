def power_of_two(upto: int):
    i = 0
    while i < upto:
        yield i * 2
        i += 1