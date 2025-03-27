import datetime as dt
from math import floor 

cost = int(input())
discount = int(input())
delivery_time = int(input())
buying_day = input()
buying_time = input()
buying_day = dt.datetime.strptime(buying_day, '%d.%m.%Y').date()
buying_time = dt.datetime.strptime(buying_time, '%H:%M').time()
day_of_week = buying_day.weekday()
left_time = dt.time(6, 00)
right_time = dt.time(12, 30)
if left_time <= buying_time <= right_time:
    cost = floor(cost * (1 - discount / 100))
    if day_of_week != 0:
        delivery_time -= 1
dt1 = dt.timedelta(days=delivery_time)
ans1 = buying_day + dt1
print(ans1.strftime("%d-%m-%Y"), cost)
        
        

