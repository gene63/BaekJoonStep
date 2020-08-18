import math
primes = []
for num in range(1,123456*2+1):
    num = int(num)
    if num == 1:
        prime = False
    else:
        prime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            prime = False
            break
    if prime:
        primes.append(num)

result = []
while(True):
    prime_list = []
    n = int(input())
    if n == 0:
        break
    for i in range(n+1,2*n+1):
        if i in primes:
            prime_list.append(i)
    result.append(len(prime_list))

for i in result:
    print(i)