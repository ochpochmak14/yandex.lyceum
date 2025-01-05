s = input()
a = s[1::].replace('V', '!V!').split('!')
current_pos = 0 
k = 1 if len(s) == 1 or s[1] == 'V' else 0
for i in a:
    if i == '':
        continue 
    elif i[0] == '<':
        current_pos -= len(i)
        print(current_pos * ' ' + s[0] + i.replace('<', s[0]))
        k = 0
    elif i[0] == '>':
        print(current_pos * ' ' + s[0] + i.replace('>', s[0]))
        current_pos += len(i)
        k = 0
    elif i[0] == 'V':
        if k:
            print(current_pos * ' ' + s[0])
        k = 1
if k:
    print(current_pos * ' ' + s[0])