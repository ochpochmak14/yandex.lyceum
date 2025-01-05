n = int(input())
numerous = list()
items = list()
for i in range(n):
    item = input()
    numer = int(input())
    items.append(item)
    numerous.append(numer)
for i in range(len(items) - 1, -1, -1):
    print(items[i], numerous[i])