import os
import re
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_pos(vx0, vy0, current_time):
    current_y = vy0 * current_time - (current_time - 1) * (current_time) // 2

    current_x = (
        (2 * vx0 - current_time + 1) * (current_time) // 2
        if current_time < vx0
        else vx0 * (vx0 + 1) // 2
    )

    return current_x, current_y


def will_intersect(current_v, upper_bound, lower_bound):
    tmin = math.floor(
        current_v[1] + math.sqrt(current_v[1] * current_v[1] - 2 * upper_bound[1])
    )
    tmax = math.floor(
        current_v[1] + math.sqrt(current_v[1] * current_v[1] - 2 * lower_bound[1])
    )

    for current_t in range(tmin, tmax + 2):
        current_x, current_y = get_pos(current_v[0], current_v[1], current_t)
        if (
            upper_bound[0] <= current_x <= lower_bound[0]
            and lower_bound[1] <= current_y <= upper_bound[1]
        ):
            return True
    return False

def load_data():
	file = "input17.txt"
	return file

def part1():
	file = load_data()
	with open(file, encoding="utf-8") as f_d:
		_, _, y_1, _ = list(map(int, re.findall(r"-?\d+", f_d.read())))
	
	print('Part1 Answer: ', abs(y_1) * (abs(y_1) - 1) // 2)

def part2():
	file = load_data()
	with open(file, encoding="utf-8") as f_d:
		x_1, x_2, y_1, y_2 = list(map(int, re.findall(r"-?\d+", f_d.read())))

	vy_min = y_1
	vx_max = x_2

	vy_max = -y_1
	vx_min = math.floor(math.sqrt(2 * x_1) - 1)

	upper_bound = (x_1, y_2)
	lower_bound = (x_2, y_1)

	tmp = sum(
        [
            will_intersect((vx, vy), upper_bound, lower_bound)
            for vx in range(vx_min, vx_max + 1)
            for vy in range(vy_min, vy_max + 1)
        ]
    )
	print('Part2 Answer: ', tmp)


if __name__ == "__main__":
    part1()
    part2()