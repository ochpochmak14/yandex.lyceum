ls = []


def refinement(arr: list) -> float:
    k = 0
    s = 0
    ls.append(arr)
    sm = 0
    for item in ls:
        for i in item:
            sm += i
    for item in ls:
        for i in item:
            if i % 2 == sm % 2:
                s += i
                k += 1
    if k != 0:
        return s / k
    return 0
