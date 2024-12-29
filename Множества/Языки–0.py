m = int(input())
n = int(input())
st1 = set()
st2 = set()
for i in range(m):
    a = input()
    st1.add(a)
for i in range(n):
    a = input()
    if a in st1:
        st1.remove(a)
    else:
        st1.add(a)
if len(st1) == 0:
    print("NO")
else:
    print(len(st1))
        
