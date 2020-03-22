a, b = input().split()
a = int(a)
b = int(b)
new = a*60+b
new = new - 45
if new < 0 :
    new = new + 24*60
print(str(int(new/60))+' '+str(new%60))