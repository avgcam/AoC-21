import os
import math
from collections import defaultdict
from queue import PriorityQueue as pq

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
	file = open('input15.txt')
	grid = []
	for x in file:
		grid.append(list(map(int, x.strip())))
	
	return grid

def part1():
    grid = load_data()

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visit = pq()
    visit.put((0, (0, 0)))

    risk = defaultdict(lambda: math.inf)
    risk[(0, 0)] = 0

    while not visit.empty():
        (r, (x, y)) = visit.get()

        for dx, dy in deltas:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                new_risk = r + grid[x + dx][y + dy]
                if risk[(x + dx, y + dy)] > new_risk:
                    risk[(x + dx, y + dy)] = new_risk
                    visit.put((risk[(x + dx, y + dy)], (x + dx, y + dy)))

    return print('Part1 Answer: ', risk[(len(grid) - 1, len(grid[0]) - 1)])

def get_risk(grid, x, y):
    tmp = grid[x % len(grid)][y % len(grid[0])] + x // len(grid) + y // len(grid[0])
    return (tmp - 1) % 9 + 1

def part2():
    grid = load_data()

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visit = pq()
    visit.put((0, (0, 0)))

    risk = defaultdict(lambda: math.inf)
    risk[(0, 0)] = 0

    while not visit.empty():
        (r, (x, y)) = visit.get()

        for dx, dy in deltas:
            if 0 <= x + dx < 5 * len(grid) and 0 <= y + dy < 5 * len(grid[0]):
                new_risk = r + get_risk(grid, x + dx, y + dy)
                if risk[(x + dx, y + dy)] > new_risk:
                    risk[(x + dx, y + dy)] = new_risk
                    visit.put((risk[(x + dx, y + dy)], (x + dx, y + dy)))

    return print('Part2 Answer: ', risk[(5 * len(grid) - 1, 5 * len(grid[0]) - 1)])

if __name__ == "__main__":
    part1()
    part2()