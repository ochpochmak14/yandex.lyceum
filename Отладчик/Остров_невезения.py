day = int(input())
month = int(input())
year = int(input())

c = year // 100
m = (month - 2) % 12
if m == 0:
    m = 12
if m == 11 or m == 12:
    year = year - 1
y = year % 100
ans = day + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
print(ans % 7)