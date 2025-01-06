word = input()
dct = {}
ls = [x for x in word.split()]
for item in ls:
    dct[item] = dct.get(item, 0) + 1 
    print(dct[item], end=' ')