a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
numbers=[0,0,0,0,0,0,0,0,0,0]
for i in d:
    numbers[int(i)] += 1

for i in numbers:
    print(i)