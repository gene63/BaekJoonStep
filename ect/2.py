nums = list(map(int, input().split()))
target = int(input())
print("nums: ", nums)
print("target: ", target)

result = []
for i, num in enumerate(nums):
    if (target - num) in nums:
        result.append(i)
        result.append(nums.index(target - num))
        break
    # else:
print(result)