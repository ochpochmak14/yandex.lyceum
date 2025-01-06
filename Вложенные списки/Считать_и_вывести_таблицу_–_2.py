n = int(input())
m = int(input())
table = list()
for i in range(n):
    bf = list()
    for j in range(m):
        item = input()
        bf.append(item)
    table.append(bf)
for item in table:
    print(*item, sep='\t')
print()
for j in range(m):
    for i in range(n):
        print(table[i][j], end='\t')
    print()