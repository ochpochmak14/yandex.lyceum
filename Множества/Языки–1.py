m = int(input())
n = int(input())
one_lungage = set()
for i in range(n + m):
    a = input()
    if a in one_lungage:
        one_lungage.remove(a)
    else:
        one_lungage.add(a)
if len(one_lungage) == 0:
    print("NO")
else:
    print(len(one_lungage))


