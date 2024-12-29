n = int(input())
prev1 = 1
prev2 = 1
current = n
if prev1 <= n:
    print(prev1)
    print(prev1)
while True:
    current = prev1 + prev2
    if current > n:
        break
    prev1, prev2 = prev2, current
    print(current)