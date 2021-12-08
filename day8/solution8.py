import os 
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
	file = open('input8.txt')
	numbies = file.read().strip().split('\n')
	numbies = [i.split(' | ') for i in numbies]

	return numbies

def part1():
	numbies = load_data()
	count = 0
	for pattern, output_val in numbies:
		for x in output_val.split():
			if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7:
				count += 1
	return print('Part1 Answer: ', count)

def part2():
	numbies = load_data()
	count = 0
	for pattern, output_val in numbies:
		digz = defaultdict(lambda: 0)
	
		for x in pattern.split():
			if len(x) == 2:
				digz[1] = set(x)
			if len(x) == 4:
				digz[4] = set(x)
			if len(x) == 3:
				digz[7] = set(x)
			if len(x) == 7:
				digz[8] = set(x)
		
		for x in pattern.split():
			if len(x) == 5 and len(set(x) & set(digz[1])) == 2:
				digz[3] = set(x)
		
		for x in pattern.split():
			if set(x) == digz[3] | digz[4]:
				digz[9] = set(x)
		
		for x in pattern.split():
			if set(x) not in digz.values() and len(x) == 6 and len(set(x) & digz[1]) == 2:
				digz[0] = set(x)
		
		for x in pattern.split():
			if len(x) == 6 and set(x) not in digz.values():
				digz[6] = set(x)
		
		for x in pattern.split():
			if len(x) == 5 and set(x) not in digz.values() and len(digz[6] - set(x)) == 1:
				digz[5] = set(x)
		
		for x in pattern.split():
			if len(x) == 5 and set(x) not in digz.values():
				digz[2] = set(x)
		
		n = ''
		for i in output_val.split():
			for x, y in digz.items():
				if set(y) == set(i):
					n += str(x)
		count += int(n)
	
	return print("Part2 Answer: ", count)


if __name__ == "__main__":
	part1()
	part2()
