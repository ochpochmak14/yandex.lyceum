import datetime as dt


def observation_day(*data):
    today = dt.date.today()
    mn = " "
    for data1 in data:
        data1 = dt.datetime.strptime(data1, "%Y-%m-%d").date()
        if data1.day % 3 != 0:
            if mn == " ":
                if (data1 - today).days >= 0:
                    mn = data1 - today
            else:
                if (data1 - today).days >= 0:
                    mn = min(mn, data1 - today)
    return (mn.days, (today + mn).weekday() + 1)
