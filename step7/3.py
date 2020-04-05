def han(n):
    res = True

    for i in range(len(str(n))-2):
        if (int(str(n)[i + 2]) - int(str(n)[i+1])) != (int(str(n)[i+1]) - int(str(n)[i])):
            res = False
    return res

n = int(input())
count = 0
for i in range(1,n+1):
    if han(i):
        count += 1

print(count)