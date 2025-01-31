dct = dict()


def add_friends(name_of_person: str, list_of_friends: list) -> None:
    if name_of_person not in dct:
        dct[name_of_person] = []
    dct[name_of_person] += list_of_friends


def are_friends(name_of_person1: str, name_of_person2: str) -> bool:
    return (name_of_person2 in dct[name_of_person1])


def print_friends(name_of_person: str) -> None:
    friends = sorted(dct[name_of_person])
    print(*friends, sep=' ')
    