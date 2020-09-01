answer1 = [['B', 'W']*4, ['W', 'B']*4, ['B', 'W']*4 , ['W', 'B']*4, ['B', 'W']*4 , ['W', 'B']*4, ['B', 'W']*4 , ['W', 'B']*4]
answer2 = [['W', 'B']*4, ['B', 'W']*4, ['W', 'B']*4, ['B', 'W']*4, ['W', 'B']*4, ['B', 'W']*4, ['W', 'B']*4, ['B', 'W']*4]
x, y = map(int, input().split())
board = [[i for i in input()] for _ in range(x)]

def count(board):
    count1 = 0
    count2 = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != answer1[i][j]:
                count1 += 1
            if board[i][j] != answer2[i][j]:
                count2 += 1
    return min(count1, count2)

min_count = 1000000000
for i in range(x-7):
    for j in range(y-7):
        slice_board = [row[j:j+8] for row in board[i:i+8]]
        slice_count = count(slice_board)
        min_count = min(min_count, slice_count)
print(min_count)