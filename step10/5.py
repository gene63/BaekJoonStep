import math
t = int(input())
input_num = []
for i in range(t):
    input_num.append(int(input()))

def prime_list(number):
    primes = []
    for num in range(2, number+1):
        prime = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                prime = False
                break
        if prime :
            primes.append(num)
    return primes

primes = prime_list(max(input_num))

for num in input_num:
    result = []
    for i in range(int(num/2),1,-1):
        if i in primes:
            if (num - i) in primes:
                result.append([i, num-i])
                break
    print(str(result[0][0]) , str(result[0][1]))