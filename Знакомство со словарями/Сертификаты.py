n = int(input())
dct = {}
for _ in range(n):
    item = input()
    ls = [x for x in item.split()]
    key = ls[0]
    value1 = int(ls[1])
    value2 = int(ls[2])
    dct[key] = [value1, value2]
st = input()
res = [int(x) for x in st.split()]
sm = sum(res)
for key, value in dct.items():
    value1 = value[0]
    value2 = value[1]
    if value1 <= sm <= value2:
        print(key)
        break