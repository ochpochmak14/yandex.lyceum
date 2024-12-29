n = int(input())
found_cat = False
for i in range(n):
    s = input()
    if ('кот' in s) or ('Кот' in s):
        found_cat = True
    if ('Пёс' in s) or ('пёс' in s):
        found_cat = False
if found_cat:
    print('МЯУ')
else:
    print('НЕТ')