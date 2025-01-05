mins = ''
maxs = ''
s1 = input()
s2 = input()
if len(s1) > len(s2):
    mins = s2
    maxs = s1
else:
    mins = s1
    maxs = s2
while True:
    a = input()
    if a == 'стоп':
        break
    if len(a) > len(maxs) and len(a) > len(maxs):
        maxs = a
    if len(a) < len(maxs) and len(a) < len(mins):
        mins = a 
ok = False
for i in mins:
    if i not in maxs:
        ok = True
        print("НЕТ")
        break
if not ok:
    print("ДА")
        