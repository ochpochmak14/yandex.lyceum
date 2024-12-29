prev = input()
while True:
    s = input()
    if prev[len(prev) - 1] != s[0]:
        print(s)
        break
    else:
        prev = s
    