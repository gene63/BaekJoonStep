import sys

time = int(sys.stdin.readline())
for i in range(0,time):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print('%d'%(a+b))