#! /usr/bin/env python3

import sys

# O(2^n) without memoization
def fibonacci(n):
    if n < 0:
        raise ValueError('n < 0')
    elif n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        print(fibonacci(n))
    except Exception as e:
        raise e
