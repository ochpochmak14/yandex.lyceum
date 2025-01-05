n = [int(x) for x in input().split()]
 
xmax = len(n)
ymax = max(n)
 
print('*' * (xmax + 2))
print('*' + ' ' * xmax + '*')
for y in range(1, ymax + 1):
    print(end='*')
    for nk in n:
        if nk >= ymax - y + 1: 
            print(end='*')
        else:
            print(end=' ')
    print('*')