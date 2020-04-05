n = int(input())
scores = []
ave = []
nums= []
for i in range(n):
    scores.append(input().split())
    linetotal = 0
    for j in range(len(scores[i])):
        scores[i][j] = int(scores[i][j])
        if j != 0 :
            linetotal += scores[i][j]
    ave.append(linetotal/scores[i][0])

for i in range(n):
    nums.append(0)
    for j in range(1,scores[i][0]+1) :
        if scores[i][j] > ave[i] :
            nums[i] += 1

    print("%2.3f%%"%(nums[i]/scores[i][0]*100))