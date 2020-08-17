n = int(input())
sum = 0
num = len(str(n))
for i in range(1,num):
    sum += 9*(10**(i-1))*(i)
new_num = n - 10**(num-1)
sum += (new_num+1)*(num)
print(sum)