n = int(input())
scores = input().split()
max = 0
total = 0
for i in range(0,n) :
    scores[i] = int(scores[i])
    if scores[i] > max :
        max = scores[i]
for i in range(0,n) :
    scores[i] = scores[i]/max*100
    total += scores[i]

print(total/n)