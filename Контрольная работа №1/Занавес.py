n = int(input())
dct = dict()
my_str = "CURTAIN"
my_str2 = my_str.lower()
for p in range(n):
    item = input()
    ls1 = [x.strip() for x in item.split()]
    mx1 = 0
    st = set()
    for itm in ls1:
        bf = set()
        for char in itm:
            if char.lower() in my_str2:
                bf.add(char.lower())
        mx1 = max(mx1, len(bf))
    for itm in ls1:
        bf = set()
        for char in itm:
            if char.lower() in my_str2:
                bf.add(char.lower()) 
        if len(bf) == mx1:
            for char in itm:
                st.add(char.upper())
            break
    dct[p] = st
print(dct)