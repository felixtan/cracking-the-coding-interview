#!/usr/bin/env python3

import sys

cache = {
    0: 0,
    1: 1
}

# O(n) using memoization
def fibonacci(n):
    if n < 0:
        raise ValueError('n < 0')
    else:
        if n in cache:
            return cache[n]
        else:
            a = cache.get(n-1, fibonacci(n-1))
            if n-1 not in cache: cache[n-1] = a

            b = cache.get(n-2, fibonacci(n-2))
            if n-2 not in cache: cache[n-2] = b

            return a + b

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        print(fibonacci(n))
    except Exception as e:
        raise e
