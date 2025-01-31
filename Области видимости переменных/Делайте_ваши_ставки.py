bets = set()


def do_bet(number: int, money: int) -> None:
    if number not in bets and money > 0 and 1 <= number <= 10:
        bets.add(number)
        print(f"Ваша ставка в размере {money} на лошадь {number} принята")
    else:
        print("Что-то пошло не так, попробуйте еще раз")
        