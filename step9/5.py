a, b, v = map(int, input().split())
if ((v-a)/(a-b)).is_integer() :
    print(int((v-a)/(a-b))+1)
else :
    print(int((v-a)/(a-b))+2)
