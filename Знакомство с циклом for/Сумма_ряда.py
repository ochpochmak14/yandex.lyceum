n = int(input())
ans = 0
num = [-1, 1]
j = 1
for i in range(n):
    a = int(input())
    ans += num[j] * a 
    j = (j + 1) % 2
print(ans)