n1 = input()
n = ''
for i in n1:
    if i == ' ':
        break
    n += i

n = int(n)

anss = list()

pw = 0
final = 0
nn = 0
for i in range(len(n1) - 1, -1, -1):
    if n1[i] == ' ':
        break
    if n1[i].isdigit():
        nn = int(n1[i])  
        final += nn * (10 ** pw)
        pw += 1

items = list()
for i in range(n):
    item = input()
    items.append(item)

fn = 0
j = 0
for item in items:
    j += 1
    num = ''

    for i in range(len(item)):
        if item[i] == ' ':
            break
        num += item[i]

    num = int(num)

    cnt = ''
    smm = int(item[item.find('=') + 1::])
    for i in range(item.find('*') + 1, len(item)):
        if item[i] == ' ':
            break
        cnt += item[i]
    if num * int(cnt) != smm:
        anss.append(j)
    fn += num * int(cnt)

print(final - fn)
print(*anss, sep=' ')
