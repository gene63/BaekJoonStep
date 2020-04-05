n = int(input())
scores = []
for i in range(n):
    ox = input()
    scores.append(0)
    count = 0
    for j in ox:
        if j =='O':
            count += 1
            scores[i] += count
        else :
            count = 0
for i in range(n):
    print(scores[i])

