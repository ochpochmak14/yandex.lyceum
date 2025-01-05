items = list()
while True:
    item = input()
    if item == '':
        break
    items.append(item.split(":"))

pswrds = input()
pswrds1 = list(pswrds.split(";"))
for item in items:  
    if item[1] in pswrds1:
        print(f"To: {item[0]}")
        st = item[4]
        if st.find(",") == -1:
            print(f"{st}, ваш пароль слишком простой, смените его.")
        else:
            print(f"{st[:st.find(",")]}, ваш пароль слишком простой, смените его.")
