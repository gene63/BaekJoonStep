def match(char):
    char_num = ord(char)-ord('A')
    if char_num < 18:
        return int((char_num)/3) + 2
    elif char_num == 18:
        return 7
    elif char_num == 19 or char_num == 20 or char_num == 21:
        return 8
    elif char_num == 22 or char_num == 23 or char_num == 24 or char_num == 25:
        return 9

string = input()
sum = 0
for char in string:
    sum += (match(char)+1)
print(sum)