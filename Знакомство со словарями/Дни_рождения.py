n = int(input())
dct = {}
for _ in range(n):
    item = input()
    ls = [x for x in item.split()]
    name = ls[0]
    month = ls[2]
    if month not in dct:
        dct[month] = []
    dct[month].append(name)
q = int(input())
for _ in range(q):
    query = input()
    if query in dct:
        dct[query] = sorted(dct[query])
        print(*dct[query], sep=' ')
    else:
        print()