def is_square(x):
    return int(x ** (1 / 2)) ** 2 == int(x)


for i in range(1, 1000):
    for j in range(i + 1, 1000):
        c = int(i**2 + j**2)
        if is_square(c) and i + j + int(c ** (1 / 2)) == 1000:
            print(i * j * int(c ** (1 / 2)))
            exit(0)
