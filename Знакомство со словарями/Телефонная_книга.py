n = int(input())
dct = {}
for _ in range(n):
    item = input()
    ls = [x for x in item.split()]
    name = ls[1]
    number = ls[0]
    if name not in dct:
        dct[name] = []
    dct[name].append(number)
q = int(input())
for _ in range(q):
    query = input()
    if query in dct:
        print(*dct[query], sep=' ')
    else:
        print("Нет в телефонной книге")