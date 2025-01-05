n = int(input())
ls = list()
for i in range(n):
    item = input()
    ls.append(item)
q = int(input())
for i in ls:
    if q > len(i):
        continue
    print(i[q - 1], end='')