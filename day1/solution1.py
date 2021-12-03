import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def readLines():
    numbers = []

    with open('input1.txt') as f:
        for line in f.readlines():
            numbers.append(int(line))

    return numbers


def part1():
    report = readLines()
    previous = None
    increases = 0

    for depth in report:
        if previous != None and depth > previous:
            increases += 1
        previous = depth

    return print('Part1 Answer: ', increases)


def part2():
    report = readLines()
    previous = None
    increases = 0

    threes = list(zip(report, report[1:], report[2:]))
    for (a, b, c) in threes:
        total = a + b + c
        if previous != None and total > previous:
            increases += 1
        previous = total

    return print('Part2 Answer: ', increases)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
