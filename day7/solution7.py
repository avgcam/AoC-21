import os
import statistics as stat

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
	file = open('input7.txt')
	hor_pos = file.read().split(',')
	hor_pos = [int(i) for i in hor_pos]
	return hor_pos

def part1():
	data_list = load_data()
	med = int(stat.median(data_list))
	x = 0
	for i in data_list:
		x += abs(i - med)
	return print('Part1 Answer: ', x)

def part2():
	x_1 = 0
	x_2 = 0
	data_list = load_data()
	mean_data = stat.mean(data_list)
	for i in data_list:
		n1 = abs(i - int(mean_data))
		n2 = abs(i - round(mean_data))
		x_1 += (n1**2 + n1) //2
		x_2 += (n2**2 + n2) //2
	p2 = min(x_1, x_2)
	return print('Answer2 Answer: ', p2)

if __name__ == "__main__":
	part1()
	part2()
