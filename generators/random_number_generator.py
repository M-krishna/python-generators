from random import randint
def random_number_generator(within: int):
    while True:
        yield randint(0, within)