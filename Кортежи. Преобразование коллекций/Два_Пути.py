n = int(input())
characteristic = list()
characteristic = [[], []]
for i in range(n):
    x = int(input())
    characteristic[0].append(x)
    characteristic[1].append(x)
k = int(input())
for i in range(k):
    num = int(input())
    ind = int(input())
    buff = int(input())
    characteristic[num - 1][ind] += buff 
cnt = 0
for i in range(len(characteristic[0])):
    if characteristic[0][i] == characteristic[1][i]:
        cnt += 1 
        
print(*characteristic[0], sep=' ')
print(*characteristic[1], sep=' ')
print(cnt)