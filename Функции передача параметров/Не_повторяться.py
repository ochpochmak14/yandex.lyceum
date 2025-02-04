import math

divisors = {}


def number_of_divisors(n: int) -> int:
    if n in divisors:
        return divisors[n]

    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1

    divisors[n] = count
    return count

