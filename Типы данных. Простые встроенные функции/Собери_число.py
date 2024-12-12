n = int(input())
b = (n // 10 % 10 + n % 10)
c = n // 100 % 10 + n // 10 % 10 

if b > c:
    print(str(b) + str(c))
else:
    print(str(c) + str(b))