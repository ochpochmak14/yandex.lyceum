import random
import string


def generate_password(m):
    x = random.randint(1, m - 2)
    y = random.randint(1, m - x - 1)
    z = m - x - y

    password = []

    i = 0
    while i < x:
        n = random.choice(string.digits)
        if n != "1" and n != "0":
            password.append(n)
            i += 1

    i = 0
    while i < y:
        u = random.choice(string.ascii_uppercase)
        if u != "I" and u != "O":
            password.append(u)
            i += 1

    i = 0
    while i < z:
        w = random.choice(string.ascii_lowercase)
        if w != "l" and w != "o":
            password.append(w)
            i += 1

    random.shuffle(password)
    return "".join(password)


def main(n, m):
    unique_passwords = set()
    while len(unique_passwords) < n:
        unique_passwords.add(generate_password(m))
    return list(unique_passwords)
