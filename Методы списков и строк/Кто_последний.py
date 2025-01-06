n = int(input())
stack = []
for i in range(n):
    line = input()
    line1 = 0
    if line != "Следующий!":
        if line.find("?") != -1:
            buf = list()
            line1 = line[19:len(line) - 1]
            buf.append(line1)
            # print(buf, stack)
            stack = buf + stack
            # print(stack)
        else:
            line1 = line[23:len(line) - 1]
            stack.append(line1)
    else:
        if len(stack) == 0:
            print("В очереди никого нет.")
        else:
            k = stack.pop()
            print(f"Заходит {k}!")
