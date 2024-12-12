pass1 = input()
pass2 = input()
ok = False
while True:

    if len(pass1) < 8:
        print('Короткий!')
        
    elif len(pass1) >= 8:
        if '123' in pass1:
            print('Простой!')
        else:
            if pass1 != pass2:
                print('Различаются.')
            else:
                print('OK')
                ok = True
                break
    if ok:
        break
    
    pass1 = input()
    pass2 = input()