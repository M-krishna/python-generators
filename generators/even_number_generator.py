def even_number_generator(upto: int):
    i = 0
    while i < upto:
        if i % 2 == 0:
            yield i
        i += 1