n = int(input())
def blank(n):
    return [[" "for i in range(n)] for i in range(n)]

def draw(n):
    if n == 3:
        return [['*', '*', '*'] , ['*', ' ', '*'], ['*', '*', '*']]
    else :
        small_pattern = draw(int(n/3))
        return [[small_pattern, small_pattern, small_pattern], [small_pattern, blank(int(n/3)),small_pattern], [small_pattern, small_pattern, small_pattern]]

print(draw(n))