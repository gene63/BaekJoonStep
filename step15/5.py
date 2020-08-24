n = int(input())
col_check = [0 for _ in range(n)]

queens = []
count = 0

def decision(board, row_index):
    count = 0
    for i in range(n):
        board[row_index][i] = 1
        if possible(board):
            if row_index == (n-1):
                count += 1
                board[row_index][i] = 0
            else:
                count += decision(board, row_index+1)
                board[row_index][i] = 0
        else :
            board[row_index][i] = 0
    return count

def possible(board):
    queens = []
    result = True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1 :
                queens.append((i,j))
    for queen in queens:
        for i in range(((-1)*n), n+1):
            if i == 0:
                continue
            elif (queen[0] + i, queen[1] + i) in queens:
                result = False
                break
            elif (queen[0] - i, queen[1] + i) in queens:
                result = False
                break
            elif (queen[0] , queen[1] + i) in queens:
                result = False
                break
            elif (queen[0] + i , queen[1]) in queens:
                result = False
                break
    return result

board = [[0 for _ in range(n)] for _ in range(n)]
print(decision(board, 0))



