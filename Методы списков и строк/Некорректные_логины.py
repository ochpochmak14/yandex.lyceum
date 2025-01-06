line = input()
logins = [x for x in line.split(',')]
valid = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789_"
ans = list()
mx = 0 
for i in logins:
    for j in i:
        if j.lower() not in valid:
            ans.append(i)
            mx = max(mx, len(i))
            break
ans = sorted(ans)
for item in ans:
    print(' ' * (mx - len(item)), item, sep='')
    