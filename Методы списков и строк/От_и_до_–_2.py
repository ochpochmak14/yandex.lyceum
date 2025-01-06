s = input()
ls = [int(x) for x in s.split()]
mk = input()
mk1 = mk.split()
m = int(mk1[0])
k = int(mk1[1])
print(sum(ls[m:k + 1]))