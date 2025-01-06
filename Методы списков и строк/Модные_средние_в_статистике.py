line = input()
ls1 = [int(x) for x in line.split()]
ls = sorted(ls1)
mx = 0
ans = 0
for item in ls:
    mx = max(mx, ls.count(item))
for item in ls:
    if ls.count(item) == mx:
        ans = item
        break
print(ls[len(ls) // 2], ans)
