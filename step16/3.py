n = int(input())
a = 1
b = 2
for _ in range(n-1):
    temp = a
    a = b
    b = (temp + a) % 15746

print(a)