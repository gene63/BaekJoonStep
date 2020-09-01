board = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i,j))

def possibles(x,y):
    possible_points = [1 for _ in range(10)]
    possible_points[0] = 0 #0은 들어갈 수 없음
    row = board[x]
    col = [r[y] for r in board]
    square = [r[(y//3)*3:(y//3)*3+3] for r in board[(x//3)*3:(x//3)*3+3]]
    for i in row :
        if i != 0:
            possible_points[i] = 0
    for i in col :
        if i != 0:
            possible_points[i] = 0
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j] != 0:
                possible_points[square[i][j]] = 0
    return possible_points


def find(index):
    if index == len(zeros):
        return 1
    else:
        possible_numbers = possibles(zeros[index][0], zeros[index][1])
        if max(possible_numbers) == 0:
            return -1
        else :
            for i in range(len(possible_numbers)) :
                if possible_numbers[i] == 1:
                    board[zeros[index][0]][zeros[index][1]] = i
                    if find(index+1) == 1:
                        return 1
                    else :
                        board[zeros[index][0]][zeros[index][1]] = 0

    return -1

find(0)
for i in range(9):
    for j in range(9):
        print(board[i][j], end=' ')
    print()





