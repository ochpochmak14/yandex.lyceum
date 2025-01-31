current_name = None
current_range = None


def setup_profile(name: str, vacation_dates: str) -> None:
    global current_name, current_range
    current_name = name
    current_range = vacation_dates


def print_application_for_leave():
    print(f"Заявление на отпуск в период {current_range}. {current_name}")
    

def print_holiday_money_claim(amount: str) -> None:
    print(f"Прошу выплатить {amount} отпускных денег. {current_name}")


def print_attorney_letter(to_whom: str) -> None:
    print(f"На время отпуска в период {current_range} моим заместителем назначается {to_whom}. {current_name}")