Memoization decorator for python 
=== 
Add @Memoized before function definition for automatic caching. 

On the first call to the function the decorator runs it with the provided parameters. Then it stores the returned result in a file. In subsequent calls to the function with the same parameters, the decorator returns the results from the cache file without calling the function. The decorator matches the function code (text) and the parameters, so if the function or the parameters change the function will be run again. 

    from memoize.memoized import Memoized
    import time

    # Memoized.readCache = False

    @Memoized(cacheDir = "/home/username/tmp") # cacheDir defaults to /tmp in Linux 
    def fibonacci(n):
        if n <= 2: return 1

        a, b = 1, 1
        k = 2
        while k < n:
            c = a + b
            a, b = b, c
            k += 1
        return b

    n = 3e5
    
    start = time.time()
    runOne = fibonacci(n)
    finish = time.time()
    print("Runtime 1: %.2f" % (finish-start))

    start = time.time()
    runTwo = fibonacci(n)
    finish = time.time()
    print("Runtime 2: %.2f" % (finish-start))

    assert runOne == runTwo

Output: 

    Runtime 1: 0.74
    Runtime 2: 0.00

Set `Memoized.readCache` to False to skip reading the cache (but store results there nonetheless). 
