from itertools import combinations

n, m = map(int, input().split())
numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

comb = list(combinations(numbers,3))
sums = []
for i in comb:
    sums.append(sum(i))

print(max([i for i in sums if i<=m]))
