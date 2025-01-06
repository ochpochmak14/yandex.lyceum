h = int(input())
w = int(input())
for i in range(h):
    mass = [input() for _ in range(w)]
    if i != 0 and i != h - 1:
        mass = sorted(mass)
    for i in range(len(mass)):
        if i != len(mass) - 1:
            print(mass[i], end='\t')
        else:
            print(mass[i])