SCORING = {
    "Яблочко": 50,
    "Зеленое_кольцо": 25,
    "Внешнее_кольцо": {1: 8, 2: 6, 3: 42, 20: 50},
    "Внутреннее_кольцо": {1: 2, 2: 16, 3: 56, 20: 3},
}


def score(a: str, b=None):
    if b is None:
        return SCORING[a]
    else:
        return SCORING[a][b]