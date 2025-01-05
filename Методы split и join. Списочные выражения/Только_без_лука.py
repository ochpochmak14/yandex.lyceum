n = int(input())
ls = list()
for i in range(n):
    item = input()
    ls.append(item)
ans = list()
for item in ls:
    if "лук" not in item:
        ans.append(item)
print(*ans, sep=', ')