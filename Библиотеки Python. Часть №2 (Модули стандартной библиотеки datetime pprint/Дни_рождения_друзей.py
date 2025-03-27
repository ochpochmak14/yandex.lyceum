import datetime as dt


n = int(input())
today_date = dt.date.today()
time_delta = dt.timedelta(days=n)
date2 = today_date + time_delta
print(date2.day, date2.month)