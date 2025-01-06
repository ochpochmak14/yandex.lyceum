sequence = input()
line = input()
sq = [x for x in sequence.split()]
line = [x for x in line.split()]
cnt = 0
for i in sq:
    if cnt == 0:
        print(line[int(i) - 1].lower().capitalize(), end=' ')
    else:
        print(line[int(i) - 1].lower(), end=' ')
    cnt += 1 