def horse(coord1, coord2):
    x1 = ord(coord1[0]) - ord("a")
    y1 = int(coord1[1])
    x2 = ord(coord2[0]) - ord("a")
    y2 = int(coord2[1])
    if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (
        abs(x1 - x2) == 1 and abs(y1 - y2) == 2
    ):
        print("True")
    else:
        print("False")
