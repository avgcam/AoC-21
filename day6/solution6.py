import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = 'input6.txt'
with open(file, 'r') as f:
    l = list(map(int, f.readline().strip().split(",")))


def new_lanternfish(l: list[int], n_days: int, n_states=9):
    states = [0] * n_states
    for x in l:
        states[x] += 1
    for _ in range(n_days):
        nb_zeros = states[0]
        states = states[1:] + [nb_zeros]
        states[6] += nb_zeros
    return sum(states)

def main():
	print("Part1 Answer: ", new_lanternfish(l, 80))
	print("Part2 Answer: ", new_lanternfish(l, 256))

if __name__ == "__main__":
	main()