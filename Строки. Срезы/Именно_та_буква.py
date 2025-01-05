s = input()
ind = int(input())
letter = input()
if len(letter) > 1 or ind > len(s) or ind <= 0:
    print("ОШИБКА")
else:
    if s[ind - 1] != letter:
        print("НЕТ")
    else:
        print("ДА")