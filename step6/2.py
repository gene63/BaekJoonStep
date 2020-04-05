numbers=[]
max = 0
maxindex = -1
for i in range(0,9):
    numbers.append(int(input()))
    if numbers[i] > max :
        max = numbers[i]
        maxindex = i+1

print(max)
print(maxindex)