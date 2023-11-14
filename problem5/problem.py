val = 1
primes = [2, 3, 5, 7, 11, 13, 17, 19][::-1]

used = [0] * 21

for i in range(21, 2, -1):
    for p in primes:
        pp = 0
        ppp = p
        while i % ppp == 0:
            pp += 1
            ppp *= p
        used[p] = max(used[p], pp)

for i in range(1, 21):
    val *= i ** used[i]

for i in range(1, 21):
    if val % i != 0:
        print(i)

print(val)
