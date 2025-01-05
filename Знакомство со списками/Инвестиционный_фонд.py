n = int(input())
ls = list()
for i in range(n):
    item = int(input())
    ls.append(item)
    
print(*ls, end='\n')
for i in ls:
    print(i * 3)