line = input()
i = 0
while i < len(line):
    curr = line[i]
    cnt = 0
    final = -1
    for j in range(i, len(line)):
        if line[j] != curr:
            final = j 
            break
        cnt += 1
    i += cnt
    print(cnt, curr)
    