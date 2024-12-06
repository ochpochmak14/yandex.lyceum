login = input()

email = input()

if '@' not in login and '@' in email:
    print("OK")
    
else:
    if '@' in login:
        print("Некорректный логин")
        
    elif '@' not in email:
        print("Некорректный адрес")