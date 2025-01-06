letters = set()
ls = list()
op = list()
while a := input():
    fr = a[0]
    sc = a[1]
    letters.add(fr)
    letters.add(sc)
    ls.append(a)
    op.append(a)

srt = list()
for i in letters:
    srt.append(i)
srt = sorted(srt)

main_ls = list()
# print(op)
for i in srt:
    bf = list()
    bf.append(i)
    for j in srt:
        temp = i + j
        if temp in op:
            bf.append(1)
        else:
            bf.append(0)
    main_ls.append(bf)

print("  ", end='')
print(*srt)

for i in range(len(main_ls)):
    print(main_ls[i][0], end=' ')
    for j in range(1, len(main_ls[i])):
        print(main_ls[i][j], end=' ')
    print()
