def find_mountain(items: list) -> tuple:
    mx = 0
    for i in range(len(items)):
        for j in range(len(items[i])):
            mx = max(mx, items[i][j])
    for i in range(len(items)):
        for j in range(len(items[i])):
            if items[i][j] == mx:
                return i, j