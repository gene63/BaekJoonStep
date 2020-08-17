string = input().upper()
set = set(string)
counts = []
for char in set:
    count = string.count(char)
    counts.append(count)

max_value = max(counts)
max_index = [i for i ,j in enumerate(counts) if j == max_value]
if len(max_index) == 1:
    print(list(set)[max_index[0]])
else :
    print('?')