n = int(input())
num5 = int(n / 5)
if (n % 5) == 0:
    print(num5)
else:
    result = -1
    for i in range(num5, -1, -1):
        num3 = (n - (i * 5)) / 3
        if num3 == int(num3):
            result = int(num3+i)
            break
    print(result)
