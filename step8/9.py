string = list(input())
for index, char in enumerate(string):
    if index + 2 < len(string):
        if char == 'd' and string[index+1] == 'z' and string[index+2] == '=':
            del string[index+1]
            del string[index+1]
            string[index] = 'N'
    if index + 1 < len(string):
        if char == 'c':
            if string[index+1] == '=' or string[index+1] == '-':
                del string[index+1]
                string[index] = 'N'
        if char == 'd':
            if string[index+1] == '-':
                del string[index+1]
                string[index] = 'N'
        if char == 'l' and string[index+1] == 'j':
            del string[index+1]
            string[index] = 'N'
        if char == 'n' and string[index+1] == 'j':
            del string[index+1]
            string[index] = 'N'
        if char == 's':
            if string[index+1] == '=':
                del string[index+1]
                string[index] = 'N'
        if char == 'z':
            if string[index+1] == '=':
                del string[index+1]
                string[index] = 'N'

print(len(string))