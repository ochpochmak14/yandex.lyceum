s = input()
answer = input()

if s[-1] == 'ь':
    if answer[0] != s[-2]:
        print("НЕВЕРНО")
    else:
        print('ВЕРНО')
else:
    if answer[0] == s[-1]:
        print('ВЕРНО')
    else:
        print("НЕВЕРНО")