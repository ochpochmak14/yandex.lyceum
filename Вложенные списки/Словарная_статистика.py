ans = list()
while a := input():
    bf = list()
    for char in a:
        bf.append(a.count(char))
    ans.append(bf)
print(ans)
    