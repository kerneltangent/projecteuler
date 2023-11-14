def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    return True


cnt = 0
ans = 0

while cnt < 10001:
    ans += 1
    if is_prime(ans):
        cnt += 1

print(ans)
