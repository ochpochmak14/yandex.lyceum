n = int(input())
ls = list()
for _ in range(n):
    item = int(input())
    ls.append(item)
ans = set()
for i in ls:
    for j in ls:
        ans.add(i - j)
ls1 = list()
for i in ans:
    ls1.append(i)
ls1.sort()
print(*ls1, sep='\n')   