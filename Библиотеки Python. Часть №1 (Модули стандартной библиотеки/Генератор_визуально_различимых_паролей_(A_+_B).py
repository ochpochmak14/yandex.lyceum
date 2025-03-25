import random
import string


def generate_password(m):
    valid_chars = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    invalid_chars = ["l", "I", "1", "o", "O", "0"]
    valid_chars = [ch for ch in valid_chars if ch not in invalid_chars]

    while True:
        password = random.sample(valid_chars, m)
        password_str = "".join(password)

        if (
            any(ch.isdigit() for ch in password_str)
            and any(ch.islower() for ch in password_str)
            and any(ch.isupper() for ch in password_str)
        ):
            return password_str


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        passwords.add(generate_password(m))
    return list(passwords)
