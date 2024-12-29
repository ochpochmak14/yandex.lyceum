n = int(input())
clons = 0
st = set()
named = set()
for i in range(n):
    a = input()
    if a not in st:
        st.add(a)
    elif a in st and a not in named:
        clons += 1 
        named.add(a)
    else:
        clons += 1 

print(clons + len(named))

    
    