line = input()
ls = [0] * 30000
curr = 0
for op in line:
    if op == '+':
        ls[curr] = (ls[curr] + 1) % 256 
    elif op == '>':
        curr = (curr + 1) % 30000
    elif op == '-':
        ls[curr] = (ls[curr] - 1) % 256 
    elif op == '.':
        print(ls[curr])
    elif op == '<':
        curr = (curr - 1) % 30000