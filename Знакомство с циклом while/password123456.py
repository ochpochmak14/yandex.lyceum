pass1 = input()
pass2 = input()

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
