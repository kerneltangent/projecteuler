ans = 0
for i in range(100, 1000):
    for j in range(i + 1, 1000):
        if str(i * j) == str(i * j)[::-1]:
            ans = max(ans, i * j)
print(ans)
