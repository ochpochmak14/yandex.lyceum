import math


radians = float(input().strip())
degrees = (radians * 180 / math.pi) % 360
print(degrees)
