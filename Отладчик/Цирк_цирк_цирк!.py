n = int(input())
turn = 0
while True:
    if n == 1:
        break
    if n % 2 != 0:
        n -= 1
        turn += 1
    else:
        n //= 2
        turn += 1
print(turn)