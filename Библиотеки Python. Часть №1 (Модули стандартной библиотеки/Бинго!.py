from random import sample


def make_bingo():
    ls = sample(range(1, 76), 25)
    nested_ls = [ls[i:i + 5] for i in range(0, 25, 5)]
    nested_ls[2][2] = 0
    return tuple(tuple(row) for row in nested_ls)
