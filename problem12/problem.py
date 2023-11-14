from functools import cache


@cache
def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    return True


def count_divs(x):
    cnt = 0
    for i in range(1, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            cnt += 1
    return cnt * 2


def triangle(x):
    return x * (x + 1) // 2


for i in range(1, 10**6):
    if count_divs(triangle(i)) > 500:
        print(triangle(i))
        break
