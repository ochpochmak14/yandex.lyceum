def template(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        print(f"Периметр: {perimeter}")
        p = perimeter / 2
        S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"Площадь: {S}")
        ok1 = "нет"
        ok2 = "нет"
        if a == b and b == c:
            ok1 = "да"
        if a == b or b == c or a == c:
            ok2 = "да"
        print(f"Равнобедренный: {ok2}")
        print(f"Равносторонний: {ok1}")
    else:
        print(None)
