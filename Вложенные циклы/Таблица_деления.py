columns = int(input())
rows = int(input())

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print(round(j / i, 7), end=' ')
    print()