last_price = ''
buy_price = -1
sell_price = ''
is_sold = False
while True:
    price = int(input())
    if price == 0:
        if not is_sold:
            if sell_price == '':
                print(buy_price, last_price, (last_price - buy_price))
        break
    if last_price != '':
        if price > last_price:
            if buy_price == -1:
                buy_price = price
        else:
            if buy_price != -1:
                sell_price = price
                is_sold = True
                print(buy_price, sell_price, (sell_price - buy_price))
                break
    last_price = price
    