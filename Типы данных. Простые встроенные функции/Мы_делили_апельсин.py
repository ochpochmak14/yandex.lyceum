a = int(input())
b = int(input())

if b == 0:
    print("Не делится!")
elif a == 0:
    print(f"Каждому по {0}")
    print(f"Осталось {0}")
elif a * b < 0 or a * b > 0:
    print(f"Каждому по {a // b}")
    print(f"Осталось {a % b}")

    

