n = int(input())
cnt1 = 0
main_ls = list()
buf = list()
while cnt1 != n:
    item = input()
    if item == '*':
        cnt1 += 1
        main_ls.append('-'.join(buf))
        buf = list()
    else:
        for j in item.split():
            buf.append(j.strip())
print(', '.join(main_ls[::-1]))