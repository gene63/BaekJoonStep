
def d(n):
    res = n
    for i in str(n):
        res += int(i)
    return res

list = [True for i in range(10000)]

for i in range(1,10001):
    if d(i) <= 10000:
        list[d(i)-1] = False

for i in range(len(list)):
    if list[i] :
        print(i+1)