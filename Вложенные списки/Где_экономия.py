n = int(input())
s = [[]] + [list(map(int, input().split())) for _ in range(n - 1)]
for a in range(0, n - 1):
    for a1 in range(a + 1, n):
        g = s[max(a, a1)][min(a, a1)]
        b = -1
        for i in range(n):
            if i != a and i != a1:
                l_new = s[max(i, a)][min(i, a)] + s[max(i, a1)][min(i, a1)]
                g, b = (l_new, i) if (g > l_new) else (g, b)
        if b != -1:
            print(a, a1)
