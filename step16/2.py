t = int(input())
mem0 = {0:1, 1:0}
def fib0(n, mem):
    if n in mem :
        return mem[n]
    else:
        mem[n] = fib0(n-1, mem) + fib0(n-2, mem)
        return mem[n]
mem1 = {0:0, 1:1}

def fib1(n, mem):
    if n in mem :
        return mem[n]
    else:
        mem[n] = fib1(n-1, mem) + fib1(n-2, mem)
        return mem[n]

for _ in range(t):
    n = int(input())
    print(fib0(n,mem0), end=' ')
    print(fib1(n,mem1))
