from memoize import Memoized
import time

@Memoized()
def fibonacci(n):
    print('Running the fibonacci() function')
    if n <= 2:
        return 1
    a, b = 1, 1
    for i in range(2, n):
        c = a + b
        a, b = b, c
    return b

n = int(3e5)

start_time = time.time()
first_run = fibonacci(n)
duration = time.time() - start_time
print("Runtime 1: %.2f" % duration)

start_time = time.time()
second_run = fibonacci(n)
duration = time.time() - start_time
print("Runtime 2: %.2f" % duration)

assert first_run == second_run
