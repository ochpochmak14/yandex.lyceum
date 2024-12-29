finalx = int(input())
finaly = int(input())

curx = 0
cury = 0
ans = 0
direction = ''

while True:
    direction = input()
    
    if direction == 'стоп':
        break
    if curx == finalx and cury == finaly:
        print(ans)
        break
    else:
        ans += 1
        df = int(input())
        if direction == 'север':
            cury += df
        elif direction == 'запад':
            curx -= df
        elif direction == 'восток':
            curx += df
        elif direction == 'юг':
            cury -= df
    if curx == finalx and cury == finaly:
        print(ans)
        break
