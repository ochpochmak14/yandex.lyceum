num = float(input())
ans = 0

while num >= 0:
    if num > 1000:
        ans += (num - 0.05 * num)
    else:
        ans += num
    num = float(input())
print(ans)