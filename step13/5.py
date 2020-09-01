n = int(input())

def is_void(num):
    if "666" in str(num):
        return True
    else:
        return False

count = 0
for i in range(100000000):
    if is_void(i):
        count += 1
        if count == n:
            print(i)
            break
