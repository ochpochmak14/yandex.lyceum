log = ['Иванов', 'Кузнецов', 'Петрова']
board = set()


def pupil_number(surname: str) -> None:
    if surname in log:
        print(log.index(surname) + 1)
    else:
        print("Такого ученика нет.")


def add_pupil(surname: str) -> None:
    global log
    if surname not in log:
        log.append(surname)
        log = sorted(log)
        print(f"Ученик {surname} добавлен.")
    else:
        print("Такой ученик уже есть в журнале.")


def to_the_blackboard(n: int) -> None:
    pupil = log[n - 1]
    if pupil in board:
        print("Сан Саныч, Вы меня уже вызывали!")
    else:
        board.add(pupil)
        print(f"{pupil}, к доске!")
    
    