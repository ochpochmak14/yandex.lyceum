s = -1
while True:
    s = int(input())
    if s == 0:
        break
    if s % 3 == 0 and s % 7 == 0:
        print('Караул!')
        break
    elif s % 3 == 0 and s % 7 != 0:
        print('несчастливое')
    elif s % 3 != 0 and s % 7 == 0:
        print('опасное')
    else:
        print(s)