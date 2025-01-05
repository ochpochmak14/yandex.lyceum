n = int(input())
ls = list()
for i in range(n):
    item = input()
    ls.append(item)
k = int(input())
ls2 = list()
for i in range(k):
    item = input()
    ls2.append(item)
for item in ls:
    ok = True
    for item2 in ls2:
        if item2 not in item:
            ok = False
            break
    if ok:
        print(item)