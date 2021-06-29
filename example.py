from memoize.memoized import Memoized
import time

# Memoized.readCache = False


@Memoized(cacheDir="/home/username/tmp")  # cacheDir defaults to /tmp in Linux
def fibonacci(n):
    if n <= 2:
        return 1

    a = 1
    b = 1
    k = 2
    while k < n:
        c = a + b
        a = b
        b = c
        k += 1

    return b


n = 3e5
start = time.time()
runOne = fibonacci(n)
finish = time.time()
print("Runtime 1: %.2f" % (finish - start))

start = time.time()
runTwo = fibonacci(n)
finish = time.time()
print("Runtime 2: %.2f" % (finish - start))

assert runOne == runTwo
