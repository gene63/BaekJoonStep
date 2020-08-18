import math
a,b = map(int, input().split())

primes = []
for num in range(a,b+1):
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

for prime in primes:
    if prime >= a:
        print(prime)
