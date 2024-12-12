num = input()
k = 0
mn = 1e9
mx = -1
while num != '!':
    num = int(num)
    if 150 <= num <= 190:
        k += 1
        mn = min(mn, num)
        mx = max(mx, num)
    num = input()
        
print(k)
print(mn, mx)
        