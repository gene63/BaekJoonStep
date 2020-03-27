a, b, c= input().split()
a = int(a)
b = int(b)
c = int(c)
if a>b :
    d = b
    b = a
    a = d
if b>c :
    d = c
    c = b
    b = d
if a>b :
    d = b
    b = a
    a = d

print(b)