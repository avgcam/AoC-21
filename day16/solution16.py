import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
	file = open('input16.txt').read().strip()
	return file

data = bin(int(load_data(), 16))[2:]
while len(data) < 4 * len(load_data()):
	data = '0' + data

def peek(data, x):
	ret = data[0][:x]
	data[0] = data[0][x:]
	return ret

SoV = 0

def parse(data):
	global SoV

	ver = int(peek(data, 3), 2)
	SoV += ver

	tid = int(peek(data, 3), 2)
	if tid == 4:
		i = []
		while True:
			count, *v = peek(data, 5)
			i += v
			if count == '0':
				break
		return int("".join(i), 2)
	l_tid = peek(data, 1)[0]
	spv = []
	if l_tid == '0':
		subpack_len = int(peek(data, 15), 2)
		subpack = [peek(data, subpack_len)]
		while subpack[0]:
			spv.append(parse(subpack))
	else:
		spv = [parse(data) for l in range(int(peek(data, 11), 2))]
	if tid == 0:
		return sum(spv)
	elif tid == 1:
		p = 1
		for t in spv:
			p*= t
		return p
	elif tid == 2:
		return min(spv)
	elif tid == 3:
		return max(spv)
	elif tid == 5:
		return int(spv[0] > spv[1])
	elif tid == 6:
		return int(spv[0] < spv[1])
	elif tid == 7:
		return int(spv[0] == spv[1])
p2 = parse([data])

print(SoV)
print(p2)

# if __name__ == "__main__":
# 	part1()
# 	part2()