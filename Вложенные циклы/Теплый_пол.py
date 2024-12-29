m = int(input())
n = int(input())
cnt = 1
for i in range(1, min(m, n) + 1):
    cnt1 = cnt + max(n, m) - 1
    for j in range(1, max(n, m) + 1):
        if i % 2 == 1:
            print(cnt, end='\t')
            cnt += 1
        else:
            print(cnt1, end='\t')
            cnt1 -= 1 
            cnt += 1
    print()