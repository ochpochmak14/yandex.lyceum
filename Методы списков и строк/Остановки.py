s = input()
ls = [int(x) for x in s.split()]
ab = input()
ls2 = [int(x) for x in ab.split()]
a = ls2[0]
b = ls2[1]
print(sum(ls[a:b]))
