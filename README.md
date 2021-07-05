Memoization decorator for python 
=== 
Add `@Memoized()` before the function definition for automatic filesystem caching. 

On the first call to the function, the decorator runs it with the provided parameters. Then it stores the returned result in a file. In subsequent calls to the function with the same parameters, the decorator returns the results from the cache file without calling the function. The decorator matches the function code (text) and the parameters, so if the function or the parameters change the function will be run again. 

```python
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
```

Output: 

    Running the fibonacci() function  # Note that this appears only once!
    Runtime 1: 0.94
    Runtime 2: 0.00

## API


Set `Memoized.readCache` to False to skip reading the cache (but store results there nonetheless). 

```python
class Memoized(cacheDir=None, debug=None)
```

* `cacheDir`: Manually set the cache dir. Defaults to the system tmp dir, which is `/tmp` for POSIX and Mac.
* `debug`: Set a truthy value to enable verbose logging to `stderr`.

