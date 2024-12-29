m = int(input())
n = int(input())


st1 = set()
ans = set()

for i in range(n):
    a = input()
    st1.add(a)

for i in range(m - 1):
    st4 = set()
    n = int(input())
    for j in range(n):
        pupil = input()
        st4.add(pupil)
    st1 = st4.intersection(st1)        
if len(st1) == 0:
    print("NO")
else:
    for i in st1:
        print(i)
    
    