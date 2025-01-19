def line(s, t):
    x = float(t.split(";")[0])
    y = float(t.split(";")[1])
    ls = s.split("x")
    k = float(ls[0])
    b = float(ls[1])
    print(y == k * x + b)