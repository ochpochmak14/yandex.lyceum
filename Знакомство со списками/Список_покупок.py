n = int(input())
ls = list()
for i in range(n):
    item = input()
    ls.append(item)
print(*ls, sep='\n')     