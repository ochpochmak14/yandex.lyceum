line = input()
op = [x for x in line.split()]
stack = []
for item in op:
    if item == '*' or item == '-' or item == '+':
        
        if item == '*':
            fr = stack.pop()
            sc = stack.pop()
            stack.append(fr * sc)
        elif item == '-':
            sc1 = stack.pop()
            fr1 = stack.pop()
            stack.append(fr1 - sc1)
        elif item == '+':
            fr = stack.pop()
            sc = stack.pop()
            stack.append(fr + sc)
    else:
        stack.append(int(item))
print(*stack)