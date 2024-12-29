ans = 1
s = ''
ok = False
while s != 'СТОП':
    s = input()
    if ('Кот' in s) or ('кот' in s):
        print(ans)
        ok = True
        break
    ans += 1

if not ok:
    print(-1)
    
    