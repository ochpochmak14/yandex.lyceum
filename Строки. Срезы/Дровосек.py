word = input()
number = int(input())

while len(word) >= 2 * number:
    print(word[-number:])
    print(word[:number])
    word = word[number:-number]    
if len(word) > number:
    print(word[-number:])
    word = word[:-number]
    print(word[:number])
else:
    print(word)
    