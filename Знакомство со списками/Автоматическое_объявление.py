n = int(input())
ls = list()
for i in range(n):
    item = input()
    ls.append(item)
q = int(input())
for i in range(q):
    num = int(input())
    print(ls[num - 1])