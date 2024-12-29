p1 = 3.141592653589793

n = int(input())
sm = 0
for i in range(1, n + 1):
    sm += 1 / i ** 2
ans = p1 ** 2 / sm
print(f'{ans:.10f}')
