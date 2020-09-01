n = int(input())
people = []
for i in range(n):
    x, y = map(int, input().split())
    people.append((x,y))

def large(a,b):
    if a[0] > b[0] and a[1] > b[1]:
        return True
    else:
        return False

for i in people:
    count = 0
    for j in people:
        if large(j, i):
            count += 1
    print(count+1, end=' ')

