n = int(input())
m = int(input())

for i in range(n, m + 1):
    ok = True
    f = i // 1000
    s = i // 100 % 10 
    t = i // 10 % 10 
    fo = i % 10 
    
    if (f == s or f == t or f == fo) or (s == t or s == fo) or t == fo:
        ok = False
    
    if ok:
        print(i)