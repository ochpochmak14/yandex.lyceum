line = input()
ls = [x.upper() for x in line.split()]
# ls2 = [x.split('') for x in ls]
for item in ls:
    buf = list()
    for j in item:
        buf.append(j)
    print('-'.join(buf), end=' ')