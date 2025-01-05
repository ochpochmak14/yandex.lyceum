n = int(input())
ls = list()
for i in range(n):
    x = int(input())
    ls.append(x)

ok = False
used = False
target = int(input())
for i in range(n):
    for j in range(n):
        if i != j:
            if ls[i] * ls[j] == target and not used:
                print("ДА")
                used = True
                ok = True
if not ok:
    print("НЕТ")