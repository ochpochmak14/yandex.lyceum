def check(a):
    sm = 0
    a1 = str(a)
    sz = len(a1)
    if sz == 1:
        return a
    else:
        j = 9
        for i in range(1, sz):
            sm += j * i
            
            j *= 10
        
        last_dig = 10 ** (sz - 1)
        sm += (a - last_dig + 1) * sz
        return sm


n = int(input())
left = 1 
r = n 
ans = 0
while left <= r:
    mid = (left + r) // 2
    if check(mid) <= n:
        ans = mid
        left = mid + 1 
    else:
        r = mid - 1 
print(ans)

        
    
    
    