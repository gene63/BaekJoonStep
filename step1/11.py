a = int(input())
b = int(input())
b1 = int(b/100)
b2 = int(int(b/10)%10)
b3 = b%10
c1 = a * b3
c2 = a * b2
c3 = a * b1
print(str(c1)+"\n"+str(c2)+"\n"+str(c3)+"\n"+str(a*b))