text = input()
a = [' *   ', '* *  ', '***  ', '* *  ', '* *  ']
b = ['**   ', '* *  ', '**   ', '* *  ', '**   ']
c = [' *   ', '* *  ', '*    ', '* *  ', ' *   ']
for j in range(5):
    for i in range(len(text)):
        if text[i] == 'A':
            print(a[j], end='')
        elif text[i] == 'B':
            print(b[j], end='')
        else:
            print(c[j], end='')
    print()