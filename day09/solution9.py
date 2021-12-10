import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def data():
    with open('input9.txt', 'r') as f:
        grid = [list(line) for line in f.read().strip().split('\n')]
    return grid

data = data()
rows, cols = len(data), len(data[0])
basins = []
explored = set()

def get_adjacent(a, b):
    adjacent = []
    for x, y in ((a-1, b), (a, b-1), (a, b+1), (a+1, b)):
        if 0 <= x < rows and 0 <= y < cols:
            adjacent.append((x, y))
    return adjacent

def get_basin_size(a, b):
    stack = [(a, b)]
    size = 0
    while stack:
        i, j = stack.pop()
        if (i, j) not in explored and data[i][j] != '9':
            stack += get_adjacent(i, j)
            explored.add((i, j))
            size += 1
    return size

def part1():
    low_points = 0
    for a in range(rows):
        for b in range(cols):
            depth = data[a][b]
            if all(depth < data[i][j] for i, j in get_adjacent(a, b)):
                low_points += int(depth) + 1
    return print('Part1 Answer: ',low_points)

def part2():
    for a in range(rows):
        for b in range(cols):
            if data[a][b] != '9':
                basins.append(get_basin_size(a, b))
    basins.sort()
    return print('Part2 Answer: ', basins[-3] * basins[-2] * basins[-1])

if __name__ == "__main__":
    part1()
    part2()
