from functools import reduce
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

beg_end = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
part1 = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
part2 = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}

def load_data():
    file = open('input10.txt').read().splitlines()
    return file

def scoring(l, stk, corrupt = True):
    if not l:
        return (not corrupt) * reduce(lambda x, y: 5*x + part2[y], stk[::-1], 0)
    elif l[0] in beg_end:
        return scoring(l[1:], [*stk, l[0]], corrupt)
    elif beg_end[stk[-1]] == l[0]:
        return scoring(l[1:], stk[:-1], corrupt)
    else:
        return corrupt * part1[l[0]]

scoring2 = sorted(filter(None, [scoring(l, [], False) for l in load_data()]))

if __name__ == "__main__":
    print('Part1 Answer: ', sum(scoring(l, []) for l in load_data()))
    print('Part2 Answer: ', scoring2[len(scoring2)//2])