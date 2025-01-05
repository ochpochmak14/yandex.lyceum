num = int(input())
s = "ABCDEFGHI"
for i in range(num, 0, -1):
    for j in range(0, num):
        print(s[j], i, sep='', end=' ')
    print()