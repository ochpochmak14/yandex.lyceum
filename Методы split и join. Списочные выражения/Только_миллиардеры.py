s = input()
ls1 = [x for x in s.split(";")]
for i in ls1:
    ls2 = i.split(',')
    buf = list()
    for j in ls2:
        if int(j) >= 1000000000:
            buf.append(j)
    print(",".join(buf))    