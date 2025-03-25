import math


n = int(input().strip())
max_distance = 0

for _ in range(n):
    x = float(input().strip())
    y = float(input().strip())
    distance = math.sqrt(x**2 + y**2)
    max_distance = max(max_distance, distance)

print(f"{max_distance:.4f}")
