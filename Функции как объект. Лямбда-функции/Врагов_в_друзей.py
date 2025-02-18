s = input()
ls = s.split("; ")


def func(word: str) -> str:
    lst = word.split()[-1]
    if lst[-3:] != "ino":
        lst = lst[:-2] + "ino"
    elif lst[-3:] == "ino":
        lst = lst[:-3] + "lone"
    return lst


print(*list(map(func, filter(lambda x: len(x.split()) > 1, ls))), sep=', ')
