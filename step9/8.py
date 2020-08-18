t = int(input())
answer = []
for _ in range(t):
    x, y = map(int, input().split())
    distance = y-x
    to_go = distance
    count = 0
    for i in range(1,2**31):
        if to_go >= 2*i:
            count += 2
            to_go -= 2*i
        elif to_go > i:
            count += 2
            to_go = to_go - to_go
            break
        elif to_go == i:
            count += 1
            to_go -= i
            break
        else :
            count += 1
            to_go = to_go - to_go
            break
    answer.append(count)
for i in answer:
    print(i)


