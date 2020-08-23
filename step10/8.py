while True:
    a,b,c = map(int, input().split())
    if a == 0:
        break
    side = [a,b,c]
    max_side = max(side)
    square_sum = 0
    for i in side:
        if i != max_side:
            square_sum += i**2
    if square_sum == (max_side**2):
        print("right")
    else:
        print("wrong")