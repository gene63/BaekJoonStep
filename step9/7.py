def popu(a,b):
    if a == 0 :
        return b
    else :
        sum = 0
        for i in range(1,b+1):
            sum += popu(a-1,i)
        return sum

apt = [[0]*15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if i == 0 :
            apt[i][j] = j
        else :
            sum = 0
            for k in range(1,j+1):
                sum += apt[i-1][k]
            apt[i][j] = sum
t = int(input())
result = []
for _ in range(t):
    k = int(input())
    n = int(input())
    result.append(apt[k][n])
for i in result:
    print(i)