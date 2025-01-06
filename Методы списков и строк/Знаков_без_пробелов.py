line = input()
ls = [x for x in line.split()]
ls2 = list()
ans = 0
for item in ls:
    ans += len(item.strip())
print(ans)