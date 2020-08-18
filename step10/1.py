n = int(input())
nums = input().split()
primes = []
for num in nums:
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

print(len(primes))
