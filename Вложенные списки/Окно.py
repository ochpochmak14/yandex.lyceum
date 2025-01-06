n = int(input())
ls = list()
for _ in range(n):
    item = int(input())
    ls.append(item)
start = int(input())
finish = int(input())
print(*[x for x in ls if start <= x <= finish], sep='\n')