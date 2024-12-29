step = int(input())
string = input()
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet2 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

for char in string:
    if alphabet.find(char) >= 0 and alphabet.find(char) <= 31:
        index = alphabet.find(char)
        print(alphabet[(index + step) % 32], end='')
    elif alphabet2.find(char) >= 0 and alphabet2.find(char) <= 31:
        index = alphabet2.find(char)
        print(alphabet2[(index + step) % 32], end='')
    else:
        print(char, end='')
        