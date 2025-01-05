n = int(input())
for i in range(n):
    s = input()
    if 'кот' in s:
        for j in range(len(s)):
            if s[j:j + 3] == 'кот' or s[j:j + 3] == 'Кот':
                print(i + 1, j + 1)
                break