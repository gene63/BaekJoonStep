n = int(input())
for i in range(n):
    r, string = input().split()
    new_string = ''
    for char in string:
        new_string += char*int(r)
    print(new_string)