n = int(input())
dct = {}
for _ in range(n):
    item = input()
    ls = [x for x in item.split()]
    name = ls[0]
    date = ls[1]
    month = ls[2]
    if month not in dct:
        dct[month] = []
    dct[month].append([int(date), name])
q = int(input())
for _ in range(q):
    item = input()
    if item not in dct:
        print()
    else:    
        dct[item] = sorted(dct[item])
        ans = ""
        for i in dct[item]:
            ans += i[1] + " " + str(i[0]) + " "
        print(ans.strip())