#!/usr/bin/env python3

import sys

# O(n)
def fibonacci(n):
    if n < 0:
        raise ValueError('n < 0')
    elif n in [0, 1]:
        return n
    else:
        a, b = 0, 1

        for i in range(2, n):
            a, b = b, a + b

        return a + b

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        print(fibonacci(n))
    except Exception as e:
        raise e
