from functools import cache


@cache
def fib(x):
    return 1 if x < 2 else fib(x - 1) + fib(x - 2)


print(sum(fib(x) for x in range(0, 34) if fib(x) % 2 == 0 and fib(x) <= (10**6 * 4)))
