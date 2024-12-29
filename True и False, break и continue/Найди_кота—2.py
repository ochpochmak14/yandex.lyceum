ans = -1
i = 1
while True:
    s = input()
    if s == 'СТОП':
        break
    else:
        if ans == -1 and ('Кот' in s or 'кот' in s):
            ans = i
            
    i += 1
if ans != -1:
    print(ans)
else:
    print(-1)