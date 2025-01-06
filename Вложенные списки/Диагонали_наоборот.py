n = int(input())
ls = list()
for i in range(n):
    line = input()
    bf = [int(x) for x in line.split(', ')]
    ls.append(bf)
sm = 0
for i in range(n):
    sm += ls[i][i]
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            sm += ls[i][j]
for i in range(n):
    ls[i][i], ls[i][n - 1 - i] = ls[i][n - 1 - i], ls[i][i]
    
for i in ls:
    print(*i, sep=' ')
print(sm)