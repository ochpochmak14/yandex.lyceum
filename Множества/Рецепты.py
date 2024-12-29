m = int(input())
products_infridge = set()
for i in range(m):
    product = input()
    products_infridge.add(product)
n = int(input())
for i in range(n):
    name_ofcookng = input()
    amount = int(input())
    is_possible = True
    for j in range(amount):
        need_product = input()
        if need_product not in products_infridge:
            is_possible = False
    if is_possible:
        print(name_ofcookng)
