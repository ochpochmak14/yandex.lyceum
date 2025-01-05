n = int(input())
ls = list()
for i in range(n):
    word = input()
    num = int(input())
    ls.append((num, word))
    
for i in range(n - 1):
    for j in range(n - i - 1):
        if ls[j][0] > ls[j + 1][0]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
nd = None
if n % 2 == 0:
    nd = n // 2 + n % 2
else:
    nd = n // 2 + n % 2 - 1
wnrs = ls[nd::]
other = ls[0:nd:]

other2 = list()
wnrs2 = list()
for i in wnrs:
    wnrs2.append(i[1])
for i in other:
    other2.append(i[1])
    
wnrs2.sort()
other2.sort()

ans = list()
ans.append(wnrs2)
ans.append(other2)
for i in ans:
    for j in i:
        print(j)
    