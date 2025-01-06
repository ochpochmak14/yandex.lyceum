n = int(input())
for i in range(n):
    item = input()
    if 'кот' in item:
        print(i + 1, item.find('кот') + 1)