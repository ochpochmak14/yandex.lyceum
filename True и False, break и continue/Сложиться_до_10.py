ans = 0
n = -1
sm = 0
while n != 0:
    if sm == 10:
        print(ans)
        break
    n = int(input())
    sm += n
    ans += 1