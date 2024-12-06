a = input()
 
b = input()

if a == b and (a == 'Быть' or a == 'Не быть'):
    print("Выбор сделан!")
    
elif (a == 'Быть' and b == 'Не быть') or (a == 'Не быть' and b == 'Быть'):
    print("Вот в чём вопрос!")
    
else:
    print("Определитесь!")
    
