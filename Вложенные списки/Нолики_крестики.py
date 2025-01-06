n = int(input())
ls = list()
O1 = False
X1 = False
for i in range(n):
    line = input()
    if 'ooo' in line:
        O1 = True
    elif 'xxx' in line:
        X1 = True
    bf = [x for x in line]
    ls.append(bf)
ls2 = list()
for j in range(n):
    bf = ""
    for i in range(n):
        bf += ls[i][j]
    ls2.append(bf)
for i in ls2:
    if 'ooo' in i:
        O1 = True
    elif 'xxx' in i:
        X1 = True
if X1:
    print('x')
elif O1:
    print('o')
else:
    print('-')
        