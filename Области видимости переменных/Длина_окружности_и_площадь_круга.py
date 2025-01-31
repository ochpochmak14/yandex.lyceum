PI = 3.14159


def circle_length(radius: float) -> float:
    return 2 * PI * radius


def circle_area(radius: float) -> float:
    return PI * radius ** 2


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))