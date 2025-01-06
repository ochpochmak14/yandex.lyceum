line = input()
operations = [x for x in line.split()]
stack = []

for item in operations:
    if item == '+':
        fr = stack.pop()
        sc = stack.pop()
        stack.append(int(fr) + int(sc))
        
    elif item == '-':
        sc = stack.pop()
        fr = stack.pop()
        stack.append(int(fr) - int(sc))
    elif item == '*':
        fr = stack.pop()
        sc = stack.pop()
        stack.append(fr * sc)
    
    elif item == '/':
        fr = stack.pop()
        sc = stack.pop()
        stack.append(sc // fr)
    
    elif item == '~':
        fr = stack.pop()
        stack.append(fr * -1)
    
    elif item == '!':
        fr = stack.pop()
        fac = 1 
        for i in range(1, fr + 1):
            fac *= i 
        stack.append(fac)
    elif item == '#':
        fr = stack.pop()
        stack.append(fr)
        stack.append(fr)
    elif item == '@':
        th = stack.pop()
        sc = stack.pop()
        fr = stack.pop()
        stack.append(sc)
        stack.append(th)
        stack.append(fr)
    else:
        stack.append(int(item))
    # print(stack)
print(*stack)