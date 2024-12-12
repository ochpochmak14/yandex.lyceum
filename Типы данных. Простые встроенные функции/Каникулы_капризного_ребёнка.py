a = input()
b = input()

if (a == 'Тула' and b != 'Пенза' and b != a) or (a != 'Тула' and a != b and b == 'Пенза'):
    print('ДА')
else:
    print('НЕТ')