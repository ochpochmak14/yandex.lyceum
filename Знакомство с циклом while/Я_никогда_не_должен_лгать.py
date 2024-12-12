prev = ''
s = ''
while True:
    prev = s 
    s = input()
    if s == '':
        break
    else:
        if len(s) >= 100 and len(s) <= 999:
            print(prev)
        elif len(s) % 2 == 0:
            print(2 * s)
        elif len(s) % 3 == 0:
            print(3 * s)
        else:
            print(s)
            