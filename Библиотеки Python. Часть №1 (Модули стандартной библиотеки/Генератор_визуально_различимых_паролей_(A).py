import random
import string


ALLOWED_CHARACTERS = ''.join(c for c in string.ascii_letters + string.digits if c not in "lI1oO0")


def generate_password(m):
    return ''.join(random.sample(ALLOWED_CHARACTERS, m))


def main(n, m):
    passwords = set()
    while len(passwords) < n:
        passwords.add(generate_password(m))
    return list(passwords)

