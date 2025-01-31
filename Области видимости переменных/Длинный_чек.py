products = list()
cnt = 0


def add_item(item_name: str, item_cost: int) -> None:
    products.append([item_name, item_cost])


def print_receipt():
    global cnt, products
    if len(products) != 0:
        cnt += 1
        print(f"Чек {cnt}. Всего предметов: {len(products)}")
        ans = 0
        for item in products:
            print(f"{item[0]} - {item[1]}")
            ans += item[1]
        products = list()
        print(f"Итого: {ans}")
        print("-----")
