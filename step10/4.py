import math
primes = []
input_num = []
while(True):
    n = int(input())
    if n == 0:
        break
    else:
        input_num.append(n)

#소수들의 리스트
for num in range(2, 2*max(input_num)+1):
    prime = True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            prime = False
            break
    if prime :
        primes.append(num)

for n in input_num:
    """
    for prime in primes:
        if prime > i and prime <2*n+1:
            result.appned(prime)
    """

    lower_prime = [i for i in primes if i > n]
    upper_prime = [i for i in lower_prime if i < 2*n+1]
    print(len(upper_prime))