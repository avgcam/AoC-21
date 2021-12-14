import os
import time
from collections import Counter, defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
	file = open("input14.txt").read().split('\n\n')
	return file

def part1():
	file = load_data()

	x = list(file[0])
	transition = {i.split(" -> ")[0]: i.split(" -> ")[1] for i in file[1].split("\n")}

	for _ in range(10):
		x1 = []
		for i in range(len(x) - 1):
			y = "".join([x[i], x[i + 1]])
			x1 += [x[i], transition[y]]
		
		x1.append(x[-1])
		x = x1

	frequency = sorted(Counter(x).values())
	
	return print("Part1 Answer: ", frequency[-1] - frequency[0])

def part2():
	file = load_data()

	transition = {i.split(" -> ")[0]: i.split(" -> ")[1] for i in file[1].split("\n")}

	pair = Counter(
		["".join([file[0][i], file[0][i + 1]]) for i in range(len(file[0]) - 1)]
	)

	for _ in range(40):
		newPair = Counter()
		for x in pair:
			newPair[x[0] + transition[x]] += pair[x]
			newPair[transition[x] + x[1]] += pair[x]
		pair = newPair
	
	frequency = defaultdict(int)

	for x in pair:
		frequency[x[0]] += pair[x]
		frequency[x[1]] += pair[x]
	
	frequency[file[0][0]] += 1
	frequency[file[0][-1]] += 1

	return print("Part2 Answer: ", (max(frequency.values()) - min(frequency.values())) // 2)

if __name__ == "__main__":
	part1()
	part2()