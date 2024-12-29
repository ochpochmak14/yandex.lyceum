n = int(input())
m = int(input())
char = input()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 or i == n:
            print(char, end='')
        else:
            if j == 1:
                print(char, end='')
            elif j == m:
                print(char, end='')
            else:
                print(' ', end='')
    print()            