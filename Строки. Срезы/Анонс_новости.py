max_len = int(input())
n = int(input())
for i in range(n):
    s = input()
    if len(s) > max_len:
        print(s[0:max_len - 3], "...", sep='')
    else:
        print(s)