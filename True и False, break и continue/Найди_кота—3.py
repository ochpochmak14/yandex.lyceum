s = ''
found_cat = False
first_cat = False
index = 0
i = 0
j = 0
while s != 'СТОП':
    i += 1 
    s = input()
    if ('кот' in s) or ('Кот' in s):
        found_cat = True
        j += 1
        if not first_cat:
            first_cat = True
            index = i
if not found_cat:
    print(j, -1)
else:
    print(j, index)