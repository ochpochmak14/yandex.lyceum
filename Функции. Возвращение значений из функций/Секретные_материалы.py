def print_document(pages: list) -> None:
    ok1 = False
    cont = True
    for item in pages:
        if "Секретно" in item:
            ok1 = True
            cont = False
        elif cont:
            print(item)
    if ok1:
        print("Дальнейшие материалы засекречены")
    else:
        print("Напечатано без купюр")