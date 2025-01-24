def catalan(n: int) -> int:
    if n == 0:
        return 1
    else:
        a = 1
        b = 2
        for i in range(2, n + 1):
            a *= i
            b *= 2 * i * (2 * i - 1)
        c = b // (a ** 2 * (n + 1))
        c1 = b % (a ** 2 * (n + 1))
        return c + c1

