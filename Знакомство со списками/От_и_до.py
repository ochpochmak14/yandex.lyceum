n = int(input())
ls = list()
for i in range(n):
    item = int(input())
    ls.append(item)
ind1 = int(input())
ind2 = int(input())
ans = 0
for i in ls[ind1 - 1:ind2]:
    ans += i
print(ans)