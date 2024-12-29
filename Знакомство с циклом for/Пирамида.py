n = int(input())
j = 0
for i in range(1, 2 * n, 2):
    spaces = ((2 * n - 1) - i) // 2
    print(spaces * ' ', end='')
    for k in range(i):
        print('*', end='')
    print(spaces * ' ')

    