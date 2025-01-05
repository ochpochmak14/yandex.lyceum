n = int(input())
ls = list()
for i in range(n):
    height = int(input())
    metall = float(input())
    ls.append((height, metall))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if ls[j] < ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]    
print(*ls, sep='\n')