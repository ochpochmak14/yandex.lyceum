n = int(input())
i = 0
while True:
    if 2 ** i == n:
        print(i)
        break
    elif 2 ** i > n:
        print('НЕТ')
        break
    i += 1