st = input()
query = input()
norm_st = st[st.find("?") + 1::]
ls = [x for x in norm_st.split('&')]
for item in ls:
    if item[:item.find('=')] == query:
        print(item[item.find('=') + 1::])
        break