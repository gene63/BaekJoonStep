# from itertools import permutations
# n = int(input())
# numbers = input().split()
# oper = input().split()
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# for i in range(len(oper)):
#     oper[i] = int(oper[i])
#
# opers = []
# for i in range(len(oper)):
#     for j in range(oper[i]):
#         opers.append(i)
#
# permute = list(permutations(opers, len(opers)))
#
# max = -1000000000
# min = 1000000000
# for i in range(len(permute)):
#     result = numbers[0]
#     for j in range(len(permute[i])):
#         if permute[i][j] == 0:
#             result += numbers[j+1]
#         elif permute[i][j] == 1:
#             result -= numbers[j+1]
#         elif permute[i][j] == 2:
#             result *= numbers[j+1]
#         else:
#             if result < 0 :
#                 result = -result
#                 result //= numbers[j+1]
#                 result = - result
#             else:
#                 result //= numbers[j+1]
#     if result > max:
#         max = result
#     if result < min:
#         min = result
#
#
# print(max)
# print(min)


n = int(input())
numbers = input().split()
a,b,c,d = map(int, input().split())

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


def calc(result, index, add, sub, mul, div):
    global n, mmax, mmin
    if index == n :
        mmax = max(result, mmax)
        mmin = min(result, mmin)

    if add :
        calc(result + numbers[index], index+1, add-1, sub, mul, div)
    if sub:
        calc(result - numbers[index], index + 1, add, sub-1, mul, div)
    if mul:
        calc(result * numbers[index], index + 1, add, sub, mul-1, div)
    if div:
        if result < 0:
            calc(-(-result // numbers[index]), index + 1, add, sub, mul, div-1)
        else:
            calc(result // numbers[index], index + 1, add, sub, mul, div - 1)

mmax = -1000000000
mmin = 1000000000
number = numbers[0]
calc(number, 1, a,b,c,d)
print(mmax)
print(mmin)
