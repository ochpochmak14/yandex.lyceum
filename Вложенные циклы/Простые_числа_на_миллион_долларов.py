def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
for i in range(2, n):
    if is_prime(i):
        print(i)
