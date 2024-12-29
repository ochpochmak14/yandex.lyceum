st1 = set()
st2 = set()

while a := input():
    st1.add(a)
while a := input():
    st2.add(a)
    
st3 = st1.intersection(st2)
if len(st3) == 0:
    print("EMPTY")
else:
    for i in st3:
        print(i)