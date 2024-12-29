n = int(input())
ans = set()
for i in range(n):
    m = int(input())
    for product in range(m):
        prd = input()
        ans.add(prd)
print(*ans, sep='\n')
        