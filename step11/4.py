n = int(input())
road = []
def hanoi(n, start, to, left):
    global road
    if n == 1 :
        road.append(str(start)+" "+ str(to))
        return 1
    else:
        return hanoi(n-1, start, left, to) + hanoi(1, start, to, left) + hanoi(n-1, left, to, start)

print(hanoi(n, 1,3,2))
for i in road:
    print(i)