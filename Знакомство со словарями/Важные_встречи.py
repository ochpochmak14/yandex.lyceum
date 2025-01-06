n = int(input())
dct = {}
for _ in range(n):
    item = input()
    items = [x for x in item.split(", ")]
    title = items[0]
    date = items[1]
    month = items[2]
    if month not in dct:
        dct[month] = []
    dct[month].append([int(date), title])
q = input()
dct[q] = sorted(dct[q])
for i in dct[q]:
    print(i[1])
# print(*dct[q], sep='\n')