import datetime as dt


def days_left(date1: str):
    curr_date = dt.date.today()
    frst_date = dt.datetime.strptime(date1, '%d.%m.%Y').date()
    return (frst_date - curr_date).days