import random
from memoize.memoized import Memoized

# Tested functions
@Memoized()
def get_random():
    return "Hello: " + str(random.random())


print(get_random())
