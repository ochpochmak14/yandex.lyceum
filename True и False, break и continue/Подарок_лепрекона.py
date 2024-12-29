good = 0
angry = 0
mood = '123'
lastword = ''
while mood != '':
    mood = input()
    if mood == 'Какой подарок?':
        if lastword == 'добрый' and good > angry:
            print('серебряный шиллинг')
        elif lastword == 'злой' and angry > good:
            print('золотой')
        else:
            print('Ах, не знаю!')
            break
        good = 0
        angry = 0
    if mood == 'добрый':
        good += 1
    if mood == 'злой':
        angry += 1 
    lastword = mood
    