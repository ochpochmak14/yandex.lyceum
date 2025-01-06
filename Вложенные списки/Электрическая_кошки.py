n, m, i, j, f = [int(input()) for _ in range(5)]
a = [[0] * n for _ in range(m)]
a[j][i] = f
k = 0
while (t := int(f**0.5)) ** 2 == f and f != 1:
    f = t
    k += 1
    x1, y1 = i - k, j - k
    x4, y4 = i + k, j + k
    for p in range(2 * k + 1):
        if 0 <= x1 + p < n and 0 <= y1 < m:
            a[y1][x1 + p] = f
        if 0 <= x1 < n and 0 <= y1 + p < m:
            a[y1 + p][x1] = f
        if 0 <= x4 - p < n and 0 <= y4 < m:
            a[y4][x4 - p] = f
        if 0 <= x4 < n and 0 <= y4 - p < m:
            a[y4 - p][x4] = f

[print(*row, sep="\t") for row in a]
