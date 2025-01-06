n = int(input())

for j in range(n):
    item1 = input()
    item2 = input()
    ls1 = [int(x) for x in item1.split(' * ')]
    ls2 = [int(x) for x in item2.split(' * ')]
    predp = ls2[len(ls2) - 2]
    buf = set()
    for i in ls1:
        if i in ls2 and i <= predp:
            buf.add(i)
    print(f"{j + 1} spots:", end=' ')
    print(*buf, sep=', ')