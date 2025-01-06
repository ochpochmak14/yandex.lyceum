sp = []
one = ['встала', 'встал', 'в', 'очередь.']
two = ['Привет,', 'будет', 'за', 'тобой.'] 
three = ['хватит', 'тут', 'стоять,', 'пошли', 'отсюда.']
for i in range(int(input())):
    b = input()
    if 'встал' in b or 'встала' in b:
        x = ''
        for j in b.split():
            if j not in one:
                x = x + j + ' '
        sp.append(x.strip())
 
    elif 'Привет,' in b:
        c = b.split('! ')[0][8:]
        index = sp.index(c)
        x = ''
        for j in b.split():
            if j not in two and '!' not in j:
                if j == c:
                    x += j + ' '
                if j not in c:
                    x += j + ' '
        sp.insert(index + 1, x.strip())
 
    elif 'хватит' in b:
        s = b.split(', ')[0]
        sp.pop(sp.index(s))
 
for i in sp:
    print(i)