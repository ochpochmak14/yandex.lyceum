n = int(input())
if n == 0:
    print(50)
elif n <= 30:
    print(int(1.5 * n))
elif n <= 70:
    print(int(1.1 * n))
else:
    print(n)