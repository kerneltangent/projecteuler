sieve = [False] * (2 * 10**6 + 1)
for i in range(2, len(sieve)):
    if not sieve[i]:
        for j in range(i * i, len(sieve), i):
            sieve[j] = True
print(sum(i for i in range(2, len(sieve)) if not sieve[i]))
