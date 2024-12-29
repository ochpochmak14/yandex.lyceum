ans = 1 
for i in range(6):
    n = int(input())
    if n == 0:
        continue 
    else:
        ans *= n
print(ans)