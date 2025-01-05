n = int(input())
ls1 = list()
for i in range(n):
    item = int(input())
    ls1.append(item)
st = ""
ok2 = True
for i in range(n):
    ok = False
    item = input()
    st1 = set()
    for j in item:
        if item.count(j) == ls1[i]:
            st1.add(j)
            ok = True
    if len(st1) == 1:
        st += list(st1)[0]
    elif len(st1) > 1 or not ok:
        ok2 = False
        ok2 = False
        print("нечленораздельно")
        break
if ok2:
    print(st)
