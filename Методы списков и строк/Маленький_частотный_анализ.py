s = input()
s = s.lower()
s1 = set(s)
cnt = list()
mx = 0
for char in s1:
    if char != ' ':
        mx = max(mx, s.count(char))
ans = list()
for i in s1:
    if i != ' ' and s.count(i) == mx:
        ans.append(i)
ans.sort()
print(ans[0])
    