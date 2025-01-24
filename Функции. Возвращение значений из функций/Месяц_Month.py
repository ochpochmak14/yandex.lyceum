def month_name(number: int, language: str) -> str:
    dct = dict()
    dct[1] = ("январь", "January")
    dct[2] = ("февраль", "February")
    dct[3] = ("март", "March")
    dct[4] = ("апрель", "April")
    dct[5] = ("май", "May")
    dct[6] = ("июнь", "June")
    dct[7] = ("июль", "July")
    dct[8] = ("август", "August")
    dct[9] = ("сентябрь", "September")
    dct[10] = ("октябрь", "October")
    dct[11] = ("ноябрь", "November")
    dct[12] = ("декабрь", "December")
    if language == "en":
        return dct[number][1]
    return dct[number][0]