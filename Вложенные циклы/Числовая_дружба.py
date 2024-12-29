def div(n):
    sma = 0 
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sma += i 
    return sma


ans = 0
for i in range(1, 10000):
    b = div(i)
    if b > i and b < 10000 and div(b) == i:
        print(i, b)

