phrases = dict()


def parrot(phrase: str) -> None:
    if phrase not in phrases:
        phrases[phrase] = 1
    else:
        if phrases[phrase] >= 1:
            print(phrase)
        else:
            phrases[phrase] += 1