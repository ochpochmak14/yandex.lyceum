a = list()
for i in range(3):
    num = int(input())
    a.append(num)
    
a.sort(reverse=True)
for i in a:
    print(i)
