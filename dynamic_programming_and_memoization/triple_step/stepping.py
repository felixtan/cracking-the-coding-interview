#!/usr/bin/env python3

import sys

def generate_ways(n):
    if n <= 0:
        raise ValueError('please enter a positive integer')

    ways = []

    def step(current_path):
        for i in [1, 2, 3]:
            next = sum(current_path) + i
            next_path = current_path + [i]

            if next == n:
                ways.append(next_path)
            elif next < n:
                step(next_path)

    step([])

    return ways

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        ways = generate_ways(n)
    except IndexError as e:
        raise IndexError('please enter a positive integer')
    except Exception as e:
        raise e

    num_ways = len(ways)
    print('%d way%s:' % (num_ways, 's' if num_ways > 1 else ''))
    
    for way in ways:
        print(way)
