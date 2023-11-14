def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


val = 600851475143
ans = 0
for i in range(2, int(val ** (1 / 2)) + 1):
    if val % i == 0 and is_prime(i):
        ans = i
        val //= i
if is_prime(val):
    ans = val
print(ans)
