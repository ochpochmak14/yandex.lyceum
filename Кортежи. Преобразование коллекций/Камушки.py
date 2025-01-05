n = int(input())
ls = list()
even = 0
odd = 0
cnteven = 0
cntodd = 0
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        even += x
        cnteven += 1 
    else:
        odd += x 
        cntodd += 1 
    ls.append(x)
allsum = even + odd
ans = list()
if allsum % 2 == 0:
    for i in range(n):
        if ls[i] % 2 == 0:
            ans.append(ls[i])
    print(allsum - even, ans)
else:
    for i in range(n):
        if ls[i] % 2 == 1:
            ans.append(ls[i])
    print(allsum - odd, ans)
