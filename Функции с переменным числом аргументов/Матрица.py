def matrix(n: int = None, m: int = None, a: int = 0):
    if m is None and n is None:
        m = 1
        n = 1
    elif n is not None and m is None:
        m = n 
    ls = [[a for _ in range(m)] for _ in range(n)]
    return ls
