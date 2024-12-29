m = int(input())
n = int(input())
home = set()
need = set()
for i in range(m):
    a = input()
    home.add(a)
for i in range(n):
    a = input()
    if a in home:
        print("YES")
    else:
        print("NO")
    