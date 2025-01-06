mtx = list()
st1 = set()
st2 = set()
st3 = set()

ans1 = list()
ans2 = list()
ans3 = list()

while a := input():
    ls1 = [int(x) for x in a.split()]
    mtx.append(ls1)
mx = 0
for i in mtx:
    for j in i:
        mx = max(mx, j)
mx1 = mx
mx = mx // 2
for i in mtx:
    for j in i:
        if j > mx and j % 2 != mx % 2:
            st1.add(j)

for i in mtx:
    string = list()
    for j in i:
        string.append(j)
    string = sorted(string)
    # med = string[len(string) // 2]
    med = sum(string) / len(string)
    for j in i:
        if j % 2 == 0 and j > med // 2 and j <= mx:
            st2.add(j)
for i in mtx:
    for j in range(len(i)):
        bf1 = [x for x in i]
        for k in range(len(mtx)):
            bf1.append(mtx[k][j])
        # print(bf1
        # bff = sorted(bff)
        # med = bf1[len(bf1) // 2]
        med = sum(bf1) / len(bf1)
            
        if int(i[j]) < med:
            st3.add(i[j])

for i in st1:
    ans1.append(i)
for i in st2:
    ans2.append(i)
for i in st3:
    ans3.append(i)

ans1 = sorted(ans1)
ans2 = sorted(ans2)
ans3 = sorted(ans3)

ans11 = [str(x) for x in ans1[::-1]]

ans22 = [str(x) for x in ans2[::-1]]
ans33 = [str(x) for x in ans3[::-1]]
print("Colossal", "_".join(ans11), end="")
print(";")
print(f"Medium", "_".join(ans22), end="")
print(";")
print("Dwarf", "_".join(ans33), end="")
print(".")
