n = int(input())
def sum_to_one (n):
    return int((n+1)*n/2)

for i in range(1000000):
    if  n <= (sum_to_one(i)):
        layer = i
        break

if layer % 2 == 1:
    under = n - sum_to_one(layer - 1)
    upper = layer + 1 - under
else :
    upper = n - sum_to_one(layer - 1)
    under = layer + 1 - upper

print(str(upper)+'/'+str(under))
