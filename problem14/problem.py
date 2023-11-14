from functools import cache


@cache
def colatz(x):
    return 1 if x == 1 else colatz(x // 2 if x % 2 == 0 else 3 * x + 1) + 1


ans = 1
for i in range(10**6, 1, -1):
    if colatz(ans) < colatz(i):
        ans = i
print(ans, colatz(ans))
