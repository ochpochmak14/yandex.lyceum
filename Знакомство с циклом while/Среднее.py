num = float(input())
ans = 0
count = 0
while num >= -300:
    count += 1
    ans += num 
    num = float(input())
print(ans / count)