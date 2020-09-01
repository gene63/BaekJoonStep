n = int(input())
mem = {0:0, 1:1}
def fib(n, remem):
    if n in remem:
        return remem[n]
    else:
        remem[n] = fib(n-1, remem) + fib(n-2, remem)
        return remem[n]
print(fib(n, mem))