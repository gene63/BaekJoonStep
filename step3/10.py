time = int(input())
for i in range(1,time+1):
    for j in range(1,time-i+1):
        print(' ', end='')
    for j in range(1,i+1):
        print('*', end='')
    print()