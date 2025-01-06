line = input()
line = line.lower()
mx = 0
for i in line:
    mx = max(mx, line.count(i))
print(mx)