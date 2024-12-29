s = input()
number = int(input())

if number <= 0 or number > len(s):
    print("ОШИБКА")
else:
    print(s[number - 1])