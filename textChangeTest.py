import random
from memoize.memoized import Memoized

# Tested functions
@Memoized()
def get_random():
    return "World: " + str(random.random())


print(get_random())
