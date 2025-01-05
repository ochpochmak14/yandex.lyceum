n = int(input())
m = int(input())
ls = list()
for i in range(n):
    x = input()
    temp = list()
    for j in range(len(x)):
        if i % 2 == 0 and j % 2 == 0:
            # print(x[j], end="")
            temp.append(x[j])
    if len(temp) != 0:
        ls.append(temp)
for i in ls:
    print(*i, sep='')