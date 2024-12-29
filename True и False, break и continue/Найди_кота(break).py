n = int(input())
ok = True
for i in range(n):
    s = input()
    if ('Кот' in s) or ('кот' in s):
        print('МЯУ')
        ok = False
        break
if ok:
    print('НЕТ')
