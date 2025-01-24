def prime(number: int) -> str:
    del_count = 0
    for delitel in range(1, int(number ** 0.5) + 1):
        del_count += (number % delitel == 0)
    if del_count == 1:
        return "Простое число"
    return "Составное число"