ctrl = float(input())
ls = list()
while True:
    a = input()
    if a == "JUPYTER":
        break
    if float(a) > ctrl:
        ls.append(float(a))
print(sum(ls) / len(ls))
