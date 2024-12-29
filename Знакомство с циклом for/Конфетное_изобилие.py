j = int(input())
n = int((2 * j) ** (1 / 2))

for k in range(n, 0, -1):
    if (2 * j + k - k ** 2) % (k * 2) == 0:
        print((2 * j - k ** 2 + k) // (k * 2))
        break