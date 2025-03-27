from datetime import datetime, timedelta


def alarm(time_str, extra_time=10):
    odd_week_times = ["8:30", "8:30", "8:30", "7:45", "8:30", "10:00", "10:00"]
    even_week_times = ["9:00", "9:00", "9:30", "9:30", "9:00", "11:00", "11:00"]

    current_date = datetime.strptime(time_str, "%Y-%m-%d")
    reference_date = datetime.strptime("2021-1-4", "%Y-%m-%d")

    total_days = (current_date - reference_date).days
    weekday_num = current_date.weekday()
    current_week = total_days // 7 + 1

    if current_week % 2:
        initial_time = odd_week_times[weekday_num]
    else:
        initial_time = even_week_times[weekday_num]

    initial_time = datetime.strptime(initial_time, "%H:%M").strftime("%H:%M")
    adjusted_time = (
        datetime.strptime(initial_time, "%H:%M") + timedelta(minutes=extra_time)
    ).strftime("%H:%M")

    if weekday_num in range(5):
        result = (initial_time, adjusted_time)
    else:
        result = (initial_time,)

    return result
