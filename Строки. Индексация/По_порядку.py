s = input()
s.lower()
ok = True
for i in range(1, len(s)):
    if ord(s[i]) < ord(s[i - 1]):
        print(s[i])
        ok = False
        break
if ok:
    print("(:_0_:)")

    