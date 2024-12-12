yes = 0
no = 0

while True:
    string = input()
    if string == '':
        break
    if string == 'да':
        yes += 1 
    else:
        no += 1 
if 0.8 * (yes + no) <= yes:
    print('Достигли')
else:
    print('Пока нет')