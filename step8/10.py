n = int(input())
count = 0
for i in range(n):
    string = list(input())
    for index, char in enumerate(string):
        if index < len(string) - 2:
            if char == string[index+1]:
                start_index = index
                end_index = index + 1
                for i in range(start_index+2, len(string)):
                    if i == (len(string)-1):
                        if string[i] == char:
                            del string[index + 1:]
                            break
                    if string[i] != char:
                        end_index = i
                        del string[index + 1:end_index]
                        break
        elif index < len(string) - 1:
            if char == string[index + 1]:
                del string[index+1]
    if len(string) == len(set(string)):
        count += 1

print(count)

