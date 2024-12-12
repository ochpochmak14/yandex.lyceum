password = input()
password2 = input()
if len(password) < 8:
    print("Короткий!")
elif len(password) >= 8 and password != password2:
    print("Различаются.")
elif len(password) >= 8 and password == password2:
    print("OK")
    