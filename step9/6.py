t = int(input())
result = []
for i in range(t):
    h, w, n = map(int, input().split())
    width = n//h+1
    height = n%h
    if height == 0 :
        height = h
        width = width -1
    result.append(height*100+width)
for i in result:
    print(i)