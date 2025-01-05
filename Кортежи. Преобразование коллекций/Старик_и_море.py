n = int(input())
ls = list()
for i in range(n):
    word = input()
    num = int(word[len(word) - 1])
    ls.append((num, word[:len(word) - 2:]))
    
for i in range(n - 1):
    if ls[i][0] < ls[i + 1][0]:
        ans = (i + 1, ls[i][1])
        print(ans)
    