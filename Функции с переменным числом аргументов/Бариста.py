def choose_coffee(*cofees: str) -> str:
    dct = {
        "Эспрессо": [1, 0, 0],
        "Капучино": [1, 3, 0],
        "Маккиато": [2, 1, 0],
        "Кофе по-венски": [1, 0, 2],
        "Латте Маккиато": [1, 2, 1],
        "Кон Панна": [1, 0, 1]
    }
    for cofee in cofees:
        if all(ingredients[i] >= dct[cofee][i] for i in range(3)):
            for i in range(3):
                ingredients[i] -= dct[cofee][i]
            return cofee
    return "К сожалению, не можем предложить Вам напиток"   