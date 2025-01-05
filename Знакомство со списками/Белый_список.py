n = int(input())
st = set()
for i in range(n):
    item = input()
    st.add(item)
k = int(input())
ls = []
for i in range(k):
    item = input()
    if item in st:
        print(item)