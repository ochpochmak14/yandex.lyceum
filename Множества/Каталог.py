n = int(input())
st = set()
for i in range(n):
    a = input()
    if a in st:
        print("ДА")
    else:
        print("НЕТ")
        st.add(a)