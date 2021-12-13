import os
from collections import defaultdict, deque

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def part1():
    grid = defaultdict(list)

    for l in open("input12.txt"):
        p = l.strip().split("-")
        if "start" in l:
            grid["start"].append(list(filter(lambda x: x != "start", p))[0])
        elif "end" in l:
            grid["end"].append(list(filter(lambda x: x != "end", p))[0])
        else:
            grid[p[1]].append(p[0])
            grid[p[0]].append(p[1])

    to_visit = deque()
    pt1_count = 0

    for i in grid["start"]:
        to_visit.append([i])

    while to_visit:
        current_path = to_visit.popleft()
        if current_path[-1] in grid["end"]:
            pt1_count += 1

        for i in grid[current_path[-1]]:
            tmp = current_path + [i]
            if i.islower() and i in current_path:
                continue
            else:
                to_visit.append(tmp)

    return print("Part1 Answer: ", pt1_count)


def lower_pattern(tmp):
    lowers = [tmp.count(i) for i in set(tmp[1:]) if i.islower()]
    count = list(filter(lambda x: x > 2, lowers))

    return len(count) == 0 and lowers.count(2) < 2

def part2():
    grid = defaultdict(list)

    for l in open("input12.txt"):
        p = l.strip().split("-")
        grid[p[1]].append(p[0])
        grid[p[0]].append(p[1])

    to_visit = deque()

    pt2_count = 0

    to_visit.append(["start"])

    while to_visit:
        current_path = to_visit.popleft()

        if current_path[-1] == "end":
            pt2_count += 1
            continue

        for i in grid[current_path[-1]]:
            if i == "start":
                continue
            tmp = current_path + [i]
            if not lower_pattern(tmp):
                continue
            else:
                to_visit.append(tmp)

    return print("Part2 Answer: ", pt2_count)

if __name__ == "__main__":
    part1()
    part2()