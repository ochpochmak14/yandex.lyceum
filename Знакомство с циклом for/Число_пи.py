n = int(input())
ans = 0

for i in range(n):
    ans += ((-1) ** i) / (2 * i + 1)
print(4 * ans)