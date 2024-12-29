first = int(input())
second = int(input())
third = int(input())
while True:
    if first == 0 and second == 0 and third == 0:
        break
    a = int(input())
    b = int(input())
    if a == 1:
        first -= b 
    elif a == 2:
        second -= b 
    elif a == 3:
        third -= b 
    print(first, second, third)