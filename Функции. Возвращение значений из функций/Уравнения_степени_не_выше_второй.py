def roots_of_quadratic_equation(a: int, b: int, c: int) -> list:
    D = b ** 2 - 4 * a * c
    if a == 0 and c != 0 and b != 0:
        return [-1 * c / b]
    if a == 0 and b == 0:
        if c == 0:
            return ["all"]
        return []
    if D < 0:
        return []
    if D == 0 and b != 0:
        x1 = (-1 * b) / (2 * a)
        return [x1]
    x1 = ((-1 * b) + (D ** 0.5)) / (2 * a)
    x2 = ((-1 * b) - (D ** 0.5)) / (2 * a)
    return [x1, x2]