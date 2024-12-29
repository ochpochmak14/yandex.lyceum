n = int(input())
numerous = 0
while True:
    st = input()
    if st == 'КОНЕЦ':
        print('МАЛОВАТО')
        break
    if numerous == n:
        print('ГОТОВО')
        break
    if ('доска' in st) or ('дощечка' in st):
        numerous += 1
        print(f'Прибили {numerous} дощечку.')