n = int(input())

a = n // 100
b = n // 10 % 10 
c = n % 10 

ls = list()

ls.append(a)
ls.append(b)
ls.append(c)

ls.sort()

sm = ls[0] + ls[2]

if sm == ls[1] * 2:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')