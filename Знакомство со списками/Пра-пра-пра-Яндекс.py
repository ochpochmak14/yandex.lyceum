n = int(input())
ls = list()
for i in range(n):
    item = input()
    ls.append(item)
q = input()
for item in ls:
    if q in item:
        print(item)