#! /usr/bin/env python3

import timeit
from recursive import fibonacci as recursive_not_memoized
from recursive_memoized import fibonacci as recursive_memoized
from iterative import fibonacci as iterative

def ordinal(n):
    try:
        n = int(n)
        i = n % 10
    except Exception as e:
        raise e

    if i == 1:
        return '%dst' % n
    elif i == 2:
        return '%dnd' % n
    elif i == 3:
        return '%drd' % n
    else:
        return '%dth' % n

def compare_perf(N = 25):
    test = 'for i in range(%d): fibonacci(i)' % N

    print('calculate the %s fibonacci number' % ordinal(N))

    print('recursive, no memoization:\t%fs' % timeit.timeit(
        setup='from __main__ import recursive_not_memoized as fibonacci',
        stmt=test,
        number=10
    ))

    print('recursive, with memoization:\t%fs' % timeit.timeit(
        setup='from __main__ import recursive_memoized as fibonacci',
        stmt=test,
        number=10
    ))

    print('iterative:\t\t\t%fs' % timeit.timeit(
        setup='from __main__ import iterative as fibonacci',
        stmt=test,
        number=10
    ))

if __name__ == '__main__':
    compare_perf()
