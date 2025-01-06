treas = dict()
for _ in range(cnt := int(input())):
    x, y = input().split()
    ind = (int(x) // 10, int(y) // 10)
    treas[ind] = treas.get(ind, 0) + 1

print(max(treas.values()))