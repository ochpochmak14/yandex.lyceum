import math
g = 9.8


def collect_stones() -> float:
    global L 
    ans = math.sqrt((L * g) / math.sin(math.radians(2 * ALPHA)))
    L += 0.5
    return ans  
    