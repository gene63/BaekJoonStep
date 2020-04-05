n = int(input())
ne = input().split()
numbers = []
max=-1000000
min=1000000
for i in ne:
    numbers.append(int(i))
    if int(i) > max :
        max = int(i)
    if int(i) < min :
        min = int(i)

print('%d %d'%(min, max))
