n = int(input())
ok = True

for i in range(n):
    s = input()
    if 'кот' in s or 'Кот' in s:
        ok = False
if ok:
    print('НЕТ')
else:
    print('МЯУ')    