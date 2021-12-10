from collections import defaultdict
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def part1():
    cnt = defaultdict(int)

    for l in open("input5.txt"):
        ps = l.split(" -> ")
        p1, p2 = tuple(map(int, ps[0].split(','))), tuple(
            map(int, ps[1].split(',')))

        if p1[0] == p2[0]:
            for y in range(min((p1[1], p2[1])), max((p1[1], p2[1])) + 1):
                cnt[(p1[0], y)] += 1
        elif p1[1] == p2[1]:
            for x in range(min((p1[0], p2[0])), max((p1[0], p2[0])) + 1):
                cnt[(x, p1[1])] += 1

    print("Part1 Answer: ", sum([1 for i in cnt if cnt[i] > 1]))

def part2():
    cnt = defaultdict(int)

    for l in open("input5.txt"):
        ps = l.split(" -> ")
        p1, p2 = tuple(map(int, ps[0].split(','))), tuple(
            map(int, ps[1].split(',')))

        if p1[0] == p2[0]:
            for y in range(min((p1[1], p2[1])), max((p1[1], p2[1])) + 1):
                cnt[(p1[0], y)] += 1
        elif p1[1] == p2[1]:
            for x in range(min((p1[0], p2[0])), max((p1[0], p2[0])) + 1):
                cnt[(x, p1[1])] += 1
        else:
            xs = range(p1[0], p2[0] +
                       1) if p1[0] < p2[0] else range(p1[0], p2[0] - 1, -1)
            ys = range(p1[1], p2[1] +
                       1) if p1[1] < p2[1] else range(p1[1], p2[1] - 1, -1)

            for x, y in zip(xs, ys):
                cnt[(x, y)] += 1

    print("Part2 Answer: ", sum([1 for i in cnt if cnt[i] > 1]))

if __name__ == "__main__":
    part1()
    part2()