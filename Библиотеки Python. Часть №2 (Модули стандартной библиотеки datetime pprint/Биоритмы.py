from datetime import datetime
from math import sin, pi


def bio_rhythm(period, days_passed):
    return sin(2.0 * pi * days_passed / period) * 100


birth_date_input = input()
birth_date = datetime.strptime(birth_date_input, "%d.%m.%Y")

calc_date_input = input()
calc_date = datetime.strptime(calc_date_input, "%d.%m.%Y")

days_difference = calc_date.toordinal() - birth_date.toordinal()

print(bio_rhythm(23, days_difference))
print(bio_rhythm(28, days_difference))
print(bio_rhythm(33, days_difference))
