n = int(input())
st1 = set()
for i in range(n):
    a = int(input())
    if (
        (a > 40 and a % 2 == 0 and a % 3 != 0)
        or (a > 40 and a % 3 == 0 and a % 2 != 0)
        or (a % 2 == 0 and a % 3 == 0 and a <= 40)
    ):
        st1.add(a)
for i in st1:
    print(i, end=" ")
