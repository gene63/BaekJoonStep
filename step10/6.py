x,y,w,h = map(int, input().split())
center = [w/2, h/2]
min_distance = max([w,h])
if x < (w/2) :
    if y <(h/2):
        if min_distance > x:
            min_distance = x
        if min_distance > y:
            min_distance = y
    else :
        if min_distance > x:
            min_distance = x
        if min_distance > (h-y):
            min_distance = (h-y)
else :
    if y <(h/2):
        if min_distance > (w-x):
            min_distance = (w-x)
        if min_distance > y:
            min_distance = y
    else :
        if min_distance > (w-x):
            min_distance = (w-x)
        if min_distance > (h-y):
            min_distance = (h-y)

print(min_distance)