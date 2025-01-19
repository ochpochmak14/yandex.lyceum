def tic_tac_toe(field):
    xwin = False
    ywin = False
    for item in field:
        X = 0
        Y = 0
        for i in item:
            if i == "x":
                X += 1
            elif i == "0":
                Y += 1
        if X == 3:
            xwin = True
            break 
        elif Y == 3:
            ywin = True
            break 
    for column in range(3):
        X = 0
        Y = 0
        for row in range(3):
            if field[row][column] == "x":
                X += 1
            elif field[row][column] == "0":
                Y += 1
        if X == 3:
            xwin = True
            break 
        elif Y == 3:
            ywin = True
            break 
    X1 = 0
    Y1 = 0
    for row in range(3):
        if field[row][row] == "x":
            X1 += 1
        elif field[row][row] == "0":
            Y1 += 1
    if X1 == 3:
        xwin = True
    elif Y1 == 3:
        ywin = True
    
    X = 0
    Y = 0
    for row in range(3):
        for column in range(3):
            if row + column == 2:
                if field[row][column] == "X":
                    X += 1
                elif field[row][column] == "0":
                    Y += 1
    if X == 3:
        xwin = True
    elif Y == 3:
        ywin = True
    if xwin:
        print("x win")
    elif ywin:
        print("0 win")
    else:
        print("draw")