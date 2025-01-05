s = input()
correct = "abcdefghijklmnopqrstuvwxyz_1234567890"
ok = True
for char in s:
    if char not in correct:
        print(f"Неверный символ: {char}")
        ok = False
        break
if ok:
    print("OK")
