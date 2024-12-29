budget = int(input())
heads = int(input())
for bulls in range(1, heads + 1):
    for cows in range(0, heads + 1):
        for j in range(0, heads + 1):
            if bulls * 20 + cows * 10 + j * 5 == budget and bulls + cows + j == heads:
                print(bulls, cows, j)
        