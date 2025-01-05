s = input()

st = set()
alph1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alph2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ls = list()
for i in s:
    st.add(i)
for i in st:
    if i in alph1:
        ls.append((i, alph1.find(i) + 1))
    elif i in alph2:
        ls.append((i, alph2.find(i) + 1))
print(*ls, sep='\n')