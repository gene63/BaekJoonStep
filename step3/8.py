time = int(input())
for i in range(1,time+1):
    a,b = input().split()
    a = int(a)
    b = int(b)
    print("Case #%d: %d + %d = %d"%(i,a,b,a+b))