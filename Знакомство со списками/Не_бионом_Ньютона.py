n = int(input())
ls = list()
for i in range(n):
    item = int(input())
    ls.append(item)
    
for i in range(1, n):
    print(ls[i] + ls[i - 1])