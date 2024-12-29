n = int(input())
sequence = ['раз', 'два', 'три', 'четыре']
curind = 0
correct = 0
while True:
    if n == 0:
        print('На сегодня хватит.')
        break
    
    else:
        s = input()
        if s == sequence[curind]:
            correct += 1
            curind = (curind + 1) % len(sequence)
        else:
            n -= 1 
            print(f'Правильных отсчётов было {correct}, но теперь вы ошиблись.')
            curind = 0
            correct = 0
            
        