n = int(input())
dct = {}
for _ in range(n):
    item = input()
    key = item[:item.find(' ')]
    value = item[item.find(' ') + 1::]
    dct[key] = value
q = int(input())
for _ in range(q):
    query = input()
    print(dct.get(query, "Нет в словаре"))