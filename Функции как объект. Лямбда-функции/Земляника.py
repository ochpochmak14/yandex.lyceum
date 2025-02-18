m = int(input())
n = int(input())
ans = 0
for _ in range(n):
    s = input()
    ls = list(filter(lambda y: y >= m, [int(x) for x in s.split()]))
    ans += sum(ls)
print(ans)