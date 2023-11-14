from functools import cache


@cache
def ways(x, y):
    if x == 0 or y == 0:
        return 1
    return ways(x - 1, y) + ways(x, y - 1)


print(ways(20, 20))
