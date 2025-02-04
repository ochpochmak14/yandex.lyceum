places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]


def allocation(ls: list) -> list:
    ans = list()
    for item in ls:
        x = item[0]
        y = item[1]
        if places[x - 1][y - 1] == 0:
            places[x - 1][y - 1] = 1
        else:
            ans.append(item)
    return ans
    