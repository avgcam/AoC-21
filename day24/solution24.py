import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
        file = 'input24.txt'
        data = open(file).read().split("inp w")
        return data

def part1():
    fs = load_data()
    fs = list(map(lambda x: x.split("\n")[1:], fs))[1:]

    mapping = {}

    z = []
    for idx in range(len(fs)):
        p1, p2, p3 = (
            int(fs[idx][3].split(" ")[2]),
            int(fs[idx][4].split(" ")[2]),
            int(fs[idx][14].split(" ")[2]),
        )
        if p1 == 1:
            z.append((idx, p3))
        elif p1 == 26:
            mapping[(idx, p2)] = z.pop()
        else:
            assert False

    z = [9] * len(fs)

    for p in mapping:
        delta = mapping[p][1] + p[1]
        # target
        # z[mapping[p][0]]  + mapping[p][1] + p[1] == z[p[0]]
        if delta < 0:
            z[p[0]] = 9 + delta
        else:
            z[mapping[p][0]] = 9 - delta

    print("".join(map(str, z)))

def part2():
    fs = load_data()
    fs = list(map(lambda x: x.split("\n")[1:], fs))[1:]

    mapping = {}

    z = []
    for idx in range(len(fs)):
        p1, p2, p3 = (
            int(fs[idx][3].split(" ")[2]),
            int(fs[idx][4].split(" ")[2]),
            int(fs[idx][14].split(" ")[2]),
        )
        if p1 == 1:
            z.append((idx, p3))
        elif p1 == 26:
            mapping[(idx, p2)] = z.pop()
        else:
            assert False

    z = [1] * len(fs)

    for p in mapping:
        delta = mapping[p][1] + p[1]
        # target
        # z[mapping[p][0]]  + mapping[p][1] + p[1] == z[p[0]]
        if delta < 0:
            z[mapping[p][0]] = 1 - delta
        else:
            z[p[0]] = 1 + delta

    print("".join(map(str, z)))


if __name__ == "__main__":
    part1()
    part2()