import random
import string


def generate_serial_number(n, m, k):
    first_part = random.choice(string.ascii_uppercase)
    second_part = random.randrange(n, m + 1, k)
    third_part = round(random.uniform(1, 9), 3)
    serial_number = f"{first_part}-{second_part}-{third_part:.3f}"
    return serial_number


n = int(input())
m = int(input())
k = int(input())

serial_number = generate_serial_number(n, m, k)
print(serial_number)
