#!/usr/bin/env python3

import sys
import math
from random import randint

def generate_grid(rows = None, cols = None):
    if not rows: rows = randint(5, 8)
    if not cols: cols = randint(5, 8)

    top_left = (0, 0)
    bottom_right = (rows-1, cols-1)
    blocks = math.floor(rows * cols / 4)
    grid = [['o'] * cols for i in range(rows)]

    def generate_block_coords():
        return (randint(0, rows-1), randint(0, cols-1))

    for i in range(blocks):
        m, n = generate_block_coords()

        while (m, n) in [top_left, bottom_right] or grid[m][n] == 'x':
            m, n = generate_block_coords()

        grid[m][n] = 'x'

    return grid

def traverse(grid):
    rows, cols = len(grid), len(grid[0])
    end = (rows-1, cols-1)
    paths = []

    def _traverse(path):
        curr = path[-1]
        right = (curr[0], curr[1] + 1)
        down = (curr[0] + 1, curr[1])
        moves = [right, down]

        for move in moves:
            if move[0] <= rows-1 and move[1] <= cols-1:
                next_path = path + [move]
                if move == end:
                    paths.append(next_path)
                elif grid[move[0]][move[1]] != 'x':
                    _traverse(next_path)

    _traverse([(0, 0)])

    return paths

if __name__ == '__main__':
    grid = generate_grid()
    print('Grid:')
    for row in grid:
        print(row)

    paths = traverse(grid)
    if paths:
        print('Paths:')
        for path in paths:
            print(path)
    else:
        print('No paths')
