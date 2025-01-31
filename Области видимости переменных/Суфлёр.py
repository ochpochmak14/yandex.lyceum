words = list()


def check(message: str) -> str:
    for word in words:
        if message in word:
            return word
    words.append(message)
    return message


def prompter(message: str) -> str:
    return check(message)
        