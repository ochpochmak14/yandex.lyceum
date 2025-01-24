def check(x_cord: int, y_cord: int) -> bool:
    return 0 <= x_cord <= 7 and 1 <= y_cord <= 8


def possible_turns(coord: str) -> list:
    x = ord(coord[0]) - ord("A")
    y = int(coord[1])
    directions = [
        (+2, +1),
        (+2, -1),
        (-2, +1),
        (-2, -1),
        (+1, +2),
        (+1, -2),
        (-1, +2),
        (-1, -2),
    ]
    ans = []
    for direction in directions:
        tox = direction[0]
        toy = direction[1]
        x_final = x + tox
        y_final = y + toy
        if check(x_final, y_final):
            ans.append(chr(x_final + ord("A")) + str(y_final))
    return sorted(ans)
