a = int(input())
b = int(input())

primes = []
for num in range(a,b+1):
    num = int(num)
    if num == 1:
        prime = False
    else:
        prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
    if prime:
        primes.append(num)

new_primes = []
for i in primes:
    if i >= a:
        new_primes.append(i)

if len(new_primes) == 0:
    print(-1)
else:
    print(sum(new_primes))
    print(min(new_primes))
