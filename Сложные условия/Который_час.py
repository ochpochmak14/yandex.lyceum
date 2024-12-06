time = input()

if time == '5' or time == '6' or time == '7' or time == '8' or time == '9' or time == '10':
    print("Утро")
elif '11' <= time <= '17':
    print("День")
elif '18' <= time <= '22' and time != '2':
    print("Вечер")
elif (time == '4' or time == '3' or time == '2' or time == '1' or time == '0' or time == '23'):
    print("Ночь")
else:
    print("Ошибка")
