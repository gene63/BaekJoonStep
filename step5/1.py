a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
score = []
score.append(a)
score.append(b)
score.append(c)
score.append(d)
score.append(e)
sum = 0
for i in range(0,5):
    if score[i] < 40:
        score[i] = 40
    sum += score[i]
print(int(sum/5))
