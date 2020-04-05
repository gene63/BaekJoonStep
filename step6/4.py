nums=[]
count = 0
bool = True
for i in range(0,10):
    nums.append(int(input())%42)
nums = set(nums)

print(len(nums))