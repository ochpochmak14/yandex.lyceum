s = input()
ls = [len(x) for x in s.split()]
ls.sort()
print(ls[len(ls) - 1])