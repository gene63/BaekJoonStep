while 1:
    try:
        a, b = input().split()
    except:
        break
    a = int(a)
    b = int(b)
    print(a+b)