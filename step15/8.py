from itertools import combinations
n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]
people = set([i for i in range(n)])
permute = set((combinations(people, n//2)))
mmin = 1000000000
for arr in permute:
    a = set(arr)
    b = people - a
    ascore = 0
    bscore = 0
    for i in list(a):
        for j in list(a):
            ascore += scores[i][j]
    for i in list(b):
        for j in list(b):
            bscore += scores[i][j]
    mmin = min(mmin, abs(ascore-bscore))
print(mmin)

