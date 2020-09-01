n = input()
def gener(n):
    sum = 0
    for i in n:
        sum += int(i)
    sum += int(n)
    return sum

answer = 0
for i in range(int(n)):
    if gener(str(i)) == int(n):
        answer = i
        break
print(answer)