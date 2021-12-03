import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def readlines():
	x = []
	with open('input2.txt') as file:
		for line in file:
			dir, n = line.rstrip().split(" ")
			n = int(n)
			x.append((dir, n))
		x = tuple(x)
	return x

def part1(x):
	depth = 0
	hor_pos = 0

	for (dir, n) in x:
		if dir == 'forward':
			hor_pos += n
		elif dir == 'up':
			depth -= n
		elif dir == 'down':
			depth += n
	return hor_pos*depth

def part2(x):
	depth = 0
	hor_pos = 0
	aim = 0

	for (dir, n) in x:
		if dir == 'forward':
			hor_pos += n
			depth += aim * n
		elif dir == 'up':
			aim -= n
		elif dir == 'down':
			aim += n
	return hor_pos*depth

def main():
    print(part1(readlines()))
    print(part2(readlines()))


if __name__ == '__main__':
	main()
