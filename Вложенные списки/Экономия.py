n = int(input())
ls = [[0] * n for _ in range(n)] 


for i in range(n - 1):
    row = [int(x) for x in input().split()]
    for j in range(len(row)):
        ls[i + 1][j] = row[j] 
        ls[j][i + 1] = row[j]


stat = input().split()
a1, a2 = int(stat[0]), int(stat[1])
mx1 = max(a1, a2)
mn1 = min(a1, a2)

length = ls[mx1][mn1]
cc = -1

for i in range(n):
    if i != a1 and i != a2:
        if length > ls[max(a1, i)][min(a1, i)] + ls[max(i, a2)][min(i, a2)]:
            length = ls[max(a1, i)][min(a1, i)] + ls[max(i, a2)][min(i, a2)]
            cc = i

if cc != -1:
    print(cc)
else:
    print(a1)
