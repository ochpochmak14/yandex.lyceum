lst = [42, 17, 34, 100501]


def rests(arg: int) -> list:
    ls = []
    for item in lst:
        ls.append(item % arg)
    return ls
    