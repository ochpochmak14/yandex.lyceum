n = int(input())
ls = list()
ls.append(0)

for i in range(1, n):
    curr = ls[0:i]
    rev = curr[::-1]
    cnt = 0
    for i in range(len(rev)):
        if rev[i] == curr[i]:
            cnt += 1 
    ls.append(cnt)
print(*ls, sep='\n')