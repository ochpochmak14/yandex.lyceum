base = ["Иван", "Юлия Иванкова"]


def hello(temp: str) -> None:
    print(f"Здравствуйте, {temp}! Вашу карту ищут...")
 
 
def search_card(name: str) -> None:
    if name in base:
        print(f"Ваша карта с номером {base.index(name) + 1} найдена")
    else:
        print("Ваша карта не найдена")