n = int(input())
pwer = 0

ans = ''
ok = False
while True:
    if n == 0: 
        break
    dig = n % 10
    if dig != 0:
        ok = True
    if ok:
        ans += str(dig)
    n //= 10
print(ans)

