#################### Iterators #######################

from iterators import Range

_range = Range(1, 10)
for i in _range:
    print(i)

#################### Iterators #######################


#################### Generators #######################

from generators import range as __range
from generators import generate_fibonacci_upto

for i in __range(1, 10):
    print(i)

for i in generate_fibonacci_upto(10):
    print(i)

#################### Generators #######################
