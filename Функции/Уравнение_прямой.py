def equation(a, b):
    xcoord1 = float(a.split(';')[0])
    ycoord1 = float(a.split(';')[1])
    xcoord2 = float(b.split(';')[0])
    ycoord2 = float(b.split(';')[1])
    if xcoord1 == xcoord2:
        print(xcoord1)
    else:
        if ycoord1 == ycoord2:
            print(ycoord1)
        else:
            k = (ycoord2 - ycoord1) / (xcoord2 - xcoord1)
            print(k, ycoord2 - k * xcoord2)