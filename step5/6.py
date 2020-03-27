n = int(input())
for i in range(0,n):
    for j in range(0,2):
        for k in range (0,n):
            if j == (k%2) :
                print('*',end='')
            else :
                print(' ',end='')
        print('')
