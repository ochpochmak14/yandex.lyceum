n = int(input())
lis = list()
for _ in range(n):
    m = int(input())
    ls = list()
    for item in range(m):
        s = input().split()[1]
        if s == '5':
            ls.append(1)
        else:
            ls.append(0)
    lis.append(any(ls))
if all(lis):
    print("YES")
else:
    print("NO")
        