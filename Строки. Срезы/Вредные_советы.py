n = int(input())
for i in range(n):
    s = input()
    if s[:3].lower() == 'не ':
        print(s[3::])
    else:
        print(s)