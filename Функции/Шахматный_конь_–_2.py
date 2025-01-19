def horse2(coord):
    x = ord(coord[0]) - ord("a")
    y = int(coord[1])
    directions = [[+1, +2], [+1, -2], [-1, +2], [-1, -2], [+2, +1], [+2, -1], [-2, +1], [-2, -1]]
    ans = set()
    valid = {"a", "b", "c", "d", "e", "f", "g", "h"}
    for item in directions:
        to_x = item[0]
        to_y = item[1]
        if chr(x + to_x + ord("a")) in valid and to_y + y >= 1 and to_y + y <= 8:
            ans.add(chr(x + to_x + ord("a")) + str(to_y + y))
    for i in ans:
        print(i)
    