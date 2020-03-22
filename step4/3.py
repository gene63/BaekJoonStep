n = int(input())
new = n
count = 0
while 1:
    n1 = int(new / 10)
    n2 = new % 10
    new = ((n1 + n2) % 10) + (n2 * 10)
    count += 1
    if new == n:
        break
print(count)
