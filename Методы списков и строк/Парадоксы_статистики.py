n = int(input())
alls = list()
med = list()
mod = list()

allist = list()

for i in range(n):
    line = input()
    ls = [int(x) for x in line.split()]
    ls = sorted(ls)
    med.append(ls[len(ls) // 2])
    allist.extend(ls)
    alls.append(ls)
# for item in alls:
#     item = sorted(item)
#     med.append(item[len(item) // 2])
#     print(item[len(item) // 2])
mxall = 0
for item in alls:
    mx = 0
    for i in item:
        mx = max(mx, item.count(i))
    for i in item:
        if item.count(i) == mx:
            mod.append(int(i))
            break
print(*med, sep=' ')
med = sorted(med)
medmed = med[len(med) // 2]
modmod = 0

mx1 = 0
for j in mod:
    mx1 = max(mx1, mod.count(j))
for j in mod:
    if mod.count(j) == mx1:
        modmod = j 
        break

allist = sorted(allist)
# print(allist)
medall = allist[len(allist) // 2]
mxx = 0
modd = 0
for i in allist:
    mxx = max(mxx, allist.count(i))
for i in allist:
    if allist.count(i) == mxx:
        modd = i
        break
print(*mod, sep=' ')
print(medmed)
print(modmod)
print(int(medall))
print(modd)