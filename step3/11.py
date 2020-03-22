a, b = input().split()
a = int(a)
b = int(b)
lst = []
L = list(map(int, input().split()))
for i in range(0,a):
    if L[i] < b :
        print('%d '%(L[i]),end='')