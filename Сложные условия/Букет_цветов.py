a = input()
b = input()
c = input()
d = input()

ans = ''
if a in d:
    ans += f"В букете есть {a}"

    if b in d:
        ans += f", {b}"
    
    if c in d:
        ans += f", {c}"


elif b in d:
    ans += f"В букете есть {b}"
    
    if c in d:
        ans += f", {c}"
        
elif c in d:
    ans += f"В букете есть {c}"
    
ans += '.'

if ans == '.':
    print("Таких цветов в букете нет.")
else:    
    print(ans)
        