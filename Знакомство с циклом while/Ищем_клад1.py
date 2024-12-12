finalx = int(input())
finaly = int(input())

curx = 0
cury = 0
ans = 0
curdir = 'север'


directions = ['север', 'восток', 'юг', 'запад']

direction_index = 0 

while True:
    if cury == finaly and curx == finalx:
        print(ans)
        print(curdir)
        break
    
    direction = input()
    ans += 1 

    if direction == 'вперёд':
        steps = int(input())
        
        if curdir == 'север':
            cury += steps
        elif curdir == 'восток':
            curx += steps
        elif curdir == 'юг':
            cury -= steps
        elif curdir == 'запад':
            curx -= steps

    elif direction == 'налево':
        direction_index = (direction_index - 1) % 4
        curdir = directions[direction_index]

    elif direction == 'направо':
        direction_index = (direction_index + 1) % 4
        curdir = directions[direction_index]

    elif direction == 'разворот':
        direction_index = (direction_index + 2) % 4
        curdir = directions[direction_index]
