n = int(input())
for i in range(n):
    s = input()
    if s[:2] == '%%':
        print(s[2::])
    elif s[:4] == '####':
        continue
    else:
        print(s)