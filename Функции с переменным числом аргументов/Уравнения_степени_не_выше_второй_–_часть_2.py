import math


def solve(*coefficients):
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None

    if len(coefficients) == 1:
        return ["all"] if coefficients[0] == 0 else []

    if len(coefficients) == 2:
        b, c = coefficients
        return [-c / b] if b != 0 else (["all"] if c == 0 else [])

    a, b, c = coefficients
    if a == 0:
        return solve(b, c)

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        sqrt_d = math.sqrt(discriminant)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        return [x1, x2]
