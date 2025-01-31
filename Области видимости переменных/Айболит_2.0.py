base = ["Иван", "Юлия Иванкова"]
query = [None, None, None]
served = []
dct = dict()


def search_window() -> int:
    for window in range(query):
        if query[window] is None:
            query[window] = 1
            return window
    return -1


def hello(name: str) -> None:
    window = search_window()
    if window == -1:
        print(f"Простите, {name}. Все окна заняты")
    else:
        dct[name] = window
        served.append(name)
        print(f"Здравствуйте, {name}! Подойдите к окошку номер {window + 1}")


def search_card(name: str) -> None:
    if name in served:
        print(f"Простите, {name}, дождитесь своей очереди")
    else:
        if name in base:
            print(f"Ваша карта с номером {base.index(name) + 1} найдена")
        else:
            print("Ваша карта не найдена")


def good_bye(name: str) -> None:
    if name in served:
        print(f"До свидания, не болейте, {name}")
        served.remove(name)
        query[dct[name]] = None
    else:
        print(f"Простите, {name}, дождитесь своей очереди")




