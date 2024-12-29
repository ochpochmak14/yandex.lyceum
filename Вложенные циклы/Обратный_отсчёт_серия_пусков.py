n = int(input())
start = 0
for i in range(1, n + 1):
    for j in range(start, -1, -1):
        print(f"Осталось секунд: {j}")
    start += 1 
    print(f"Пуск {i}")