dct = {}
while item := input():
    ls = [x for x in item.split(": ")]
    dct[ls[0]] = dct.get(ls[0], 0) + int(ls[1])
print(dct)