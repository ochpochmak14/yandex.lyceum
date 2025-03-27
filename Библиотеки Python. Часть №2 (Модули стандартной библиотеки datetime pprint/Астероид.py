import datetime as dt


def asteroid_angle(divisor):
    current_date = dt.date.today()
    reference_date = dt.date(2000, 1, 1)
    days_difference = (current_date - reference_date).days
    angle = round((360 * (days_difference % divisor)) / divisor)
    return angle
