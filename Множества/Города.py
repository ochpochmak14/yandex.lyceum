n = int(input())
st = set()
for i in range(n):
    a = input()
    st.add(a)
city = input()
if city in st:
    print("TRY ANOTHER")
else:
    print("OK")