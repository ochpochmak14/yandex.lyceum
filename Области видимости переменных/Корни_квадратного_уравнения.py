def larger_root(p: float, q: float) -> float:
    d = discriminant(1, p, q) ** 0.5
    return (-p + d) / 2
 
 
def smaller_root(p: float, q: float) -> float:
    d = discriminant(1, p, q) ** 0.5
    return (-p - d) / 2
 
 
def discriminant(a: float, b: float, c: float) -> float:
    return (b ** 2) - (4 * a * c)
 
 
def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))