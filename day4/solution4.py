import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    with open('input4.txt') as x:
        print("Part1 Answer: ", part1(x))
    with open('input4.txt') as x:
        print("Part2 Answer: ", part2(x))

def part1(x):
    rand_num = []
    boards = []
    board_num = 0
    boardData = {}
    boardLength = None

    for line in x:
        if len(rand_num) == 0:
            for num in line.strip().split(','):
                rand_num.append(int(num))
        else:
            if len(boards) == 0 and len(line.strip()) == 0:
                continue
            if len(line.strip()) == 0:
                board_num += 1
                continue
            if boardLength is None:
                boardLength = len([i for i in line.split()])

            if board_num == len(boards):
                boards.append([])

            boards[board_num].append([[int(num), 0] for num in line.split()])


    bingo = False
    bingo_sum = 0
    for num in rand_num:
        for board in boards:
            board = mark(board, num)
            if check(board):
                bingo = True
                for row in board:
                    for x in row:
                        bingo_sum += x[0] if x[1]==0 else 0
                return bingo_sum*num


def mark(board, n):
    for row in board:
        for num in row:
            if num[0] == n:
                num[1] = 1

    return board

def check(board):
    for row in board:
        sum = 0
        for num in row:
            sum += num[1]
        if sum == len(row):
            return True
    
    for i in range(len(board[0])):
        sum = 0
        for row in board:
            sum += row[i][1]
        if sum == len(board[0]):
            return True

def part2(x):
    rand_num = []
    boards = []
    board_num = 0
    boardData = {}
    boardLength = None

    for line in x:
        if len(rand_num) == 0:
            for num in line.strip().split(','):
                rand_num.append(int(num))
        else:
            if len(boards) == 0 and len(line.strip()) == 0:
                continue
            if len(line.strip()) == 0:
                board_num += 1
                continue
            if boardLength is None:
                boardLength = len([i for i in line.split()])

            if board_num == len(boards):
                boards.append([])

            boards[board_num].append([[int(num), 0] for num in line.split()])


    bingo = False
    bingo_num = 0
    bingo_sum = 0
    for num in rand_num:
        for i in range(len(boards)-1, -1, -1):
            board = boards[i]
            board = mark(board, num)
            if check(board):
                if len(boards) != 1:
                    boards.remove(board)
                else:
                    bingo_num = num
                    bingo = True
                    break
        if bingo:
            break

    sum =0
    for row in boards[0]:
        for num in row:
            bingo_sum += num[0] if num[1]==0 else 0
    return bingo_sum * bingo_num


if __name__=='__main__':
    main()
