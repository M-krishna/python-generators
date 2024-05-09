#################### Iterators #######################

from iterators import Range

_range = Range(1, 10)
for i in _range:
    print(i)

#################### Iterators #######################


#################### Generators #######################

from generators import *
from generators import range as __range

for i in __range(1, 10):
    print(i)

for i in generate_fibonacci_upto(10):
    print(i)

for i in even_number_generator(10):
    print(i)

for i in power_of_two(4):
    print(i)

for i in random_number_generator(4):
    print(i)

#################### Generators #######################
