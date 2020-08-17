n = int(input())
def layer(n):
    for i in range(100000):
        total = 6*(i+1)*i/2 + 1
        if n <= total:
            return i+1
print(layer(n))