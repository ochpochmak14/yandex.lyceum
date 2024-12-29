n = int(input())
while True:
    if n == 0:
        break
    a = int(input())
    if a > 3 or a < 1 or a > n:
        print(n)
    else:
        n = n - a 
        print(n)